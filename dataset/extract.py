from pathlib import Path
from PIL import Image
import csv
from colorama import Fore, Style
from pytesseract import image_to_string
import easyocr
import os

#os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

def extract_color_middle(image: Image) -> tuple:
    """
    This function takes an image as input and returns the color of the central pixel
    """
    width, height = image.size
    central_pixel = image.getpixel((width // 2, height // 2))
    return central_pixel

def extract_color_upper_right(image: Image, padding=10) -> tuple:
    """
    This function takes an image as input and returns the color of the upper right corner
    with the specified padding from the top and bottom.
    """
    width, height = image.size
    right_x = width - padding
    upper_y = height - padding
    upper_right_pixel = image.getpixel((right_x, upper_y))
    return upper_right_pixel

def extract_text(image: Image, path: Path) -> tuple:
    """
    This function takes an image as input and returns the text shown in the image using OCR
    """
    pytesseract_text = image_to_string(image)
    reader = easyocr.Reader(['en'])
    easyocr_text = " ".join(reader.readtext(str(path), paragraph=True, detail=0))
    return pytesseract_text, easyocr_text

def is_color_kind_of_white(color, threshold=200):
    """
    Check if a color is kind of white based on a threshold value.
    Returns True if the color is considered white, otherwise False.
    """
    # Unpack the color values (R, G, B, A)
    red, green, blue = color

    # Check if all RGB values are above the threshold
    return red > threshold and green > threshold and blue > threshold

def save_to_csv(data: list):
    with open('data.csv', mode='w') as csv_file:
        fieldnames = ['color', 'tessract_text', 'easyocr_text']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def split_image(image_path:str, cols:int, rows:int):
    """
    This function takes an image path, number of columns, and number of rows as input parameters.
    It splits the image into the specified number of columns and rows,
    extracts the color of the upper right corner pixel of each piece,
    extracts the text shown in the piece and
    saves each piece in the output folder
    """
    im = Image.open(image_path)
    width, height = im.size
    piece_width, piece_height = width // cols, height // rows

    output_folder = Path("image_chunks")
    output_folder.mkdir(exist_ok=True)

    data = []
    for row in range(rows):
        for col in range(cols):
            left, top = col * piece_width, row * piece_height
            right, bottom = (col + 1) * piece_width, (row + 1) * piece_height
            piece = im.crop((left, top, right, bottom))
            piece_path = output_folder / f"piece_{row}_{col}.jpg"
            piece.save(piece_path)
            print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Saved {piece_path}")
            # Extract the color of the central pixel
            color_pixel = extract_color_upper_right(piece)
            print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Upper Right pixel color: {color_pixel}")
            # Check if the color is kind of white
            if is_color_kind_of_white(color_pixel):
                os.remove(piece_path)
                continue
            # Extract the text shown in the piece
            tessract_text, easyocr_text = extract_text (piece, piece_path)
            print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Extracted text with tesseract: {tessract_text}")
            print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Extracted text with easyocr: {easyocr_text}")
            # Store the color and text in a dictionary
            data.append({'color': color_pixel, 'tessract_text': tessract_text, 'easyocr_text': easyocr_text})
    # Pass the list of dictionaries to the save_to_csv function
    save_to_csv(data)

def main():
    COLS, ROWS = 6, 55
    split_image("image.png", COLS, ROWS)

if __name__ == "__main__":
    #print(os.getenv('KMP_DUPLICATE_LIB_OK'))
    main()
