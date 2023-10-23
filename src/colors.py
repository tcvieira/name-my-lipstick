import colorspacious as cs
import numpy as np
import ast  # For parsing the RGB tuples from string to Python tuple
import matplotlib.colors as mcolors

# TODO: refactor to use dict instead of two arrays
RGB_ORIGINAL_COLORS = [(173, 94, 89), (236, 94, 58), (210, 87, 141), (130, 26, 27), (176, 98, 96), (228, 88, 53), (118, 199, 242), (183, 70, 116), (72, 28, 25), (185, 80, 76), (213, 89, 65), (52, 97, 180), (194, 60, 110), (176, 107, 91), (203, 83, 67), (39, 29, 102), (222, 59, 124), (188, 116, 102), (241, 152, 158), (200, 90, 73), (36, 22, 57), (207, 49, 107), (184, 113, 91), (240, 149, 154), (212, 45, 36), (207, 68, 49), (15, 15, 39), (103, 28, 59), (159, 95, 85), (229, 132, 141), (197, 58, 53), (179, 85, 60), (61, 30, 45), (190, 144, 121), (215, 124, 133), (196, 53, 45), (167, 154, 174), (154, 125, 111), (208, 113, 119), (180, 46, 37), (144, 113, 154), (111, 44, 62), (139, 106, 89), (204, 104, 116), (175, 52, 45), (219, 162, 145), (133, 106, 137), (95, 31, 48), (23, 59, 71), (199, 94, 108), (151, 43, 40), (202, 151, 132), (158, 118, 181), (85, 41, 58), (75, 40, 62), (149, 30, 24), (195, 132, 117), (114, 62, 147), (60, 20, 29), (225, 71, 167), (218, 158, 158), (134, 39, 35), (195, 127, 116), (75, 38, 90), (165, 49, 110), (226, 150, 152), (199, 131, 112), (120, 37, 57), (98, 20, 59), (218, 138, 139), (198, 127, 109), (120, 33, 42), (173, 56, 85), (209, 137, 138), (215, 88, 82), (215, 143, 121), (215, 124, 217), (79, 25, 36), (154, 31, 49), (187, 121, 123), (217, 81, 69), (221, 139, 115), (158, 50, 172), (82, 29, 37), (187, 108, 114), (228, 68, 52), (135, 50, 135), (218, 156, 171), (40, 34, 34), (183, 97, 100), (234, 51, 37), (117, 55, 122), (217, 132, 151), (164, 94, 96), (198, 55, 38), (196, 133, 98), (63, 37, 64), (192, 101, 119), (190, 94, 98), (164, 62, 50), (180, 124, 101), (164, 76, 92), (180, 47, 48), (208, 118, 118), (151, 47, 38), (174, 117, 90), (165, 77, 151), (131, 55, 65), (74, 70, 87), (203, 115, 113), (171, 109, 84), (130, 42, 103), (136, 46, 120), (211, 112, 106), (154, 91, 73), (89, 31, 71), (221, 75, 122), (215, 67, 115), (239, 133, 133), (225, 149, 133), (168, 97, 79), (73, 29, 62), (218, 73, 116), (192, 90, 111), (235, 119, 120), (233, 138, 120), (181, 99, 75), (57, 30, 49), (232, 69, 112), (238, 105, 106), (218, 122, 110), (167, 86, 65), (183, 52, 86), (201, 46, 50), (224, 99, 103), (211, 115, 101), (142, 84, 62), (176, 129, 161), (180, 56, 82), (128, 52, 62), (205, 80, 86), (202, 94, 82), (139, 78, 59), (205, 140, 183), (153, 51, 75), (111, 41, 43), (151, 75, 59), (216, 106, 179), (229, 49, 48), (208, 129, 114), (88, 36, 23), (150, 77, 123), (221, 167, 141), (191, 39, 34), (181, 102, 87), (66, 28, 15), (65, 32, 53), (230, 135, 117), (179, 39, 40), (157, 83, 74), (233, 138, 94), (189, 61, 61), (145, 71, 62), (155, 125, 117), (205, 91, 150), (217, 109, 135), (110, 52, 30), (170, 60, 63), (139, 62, 52), (134, 96, 85), (196, 99, 144), (233, 102, 134), (162, 46, 47), (134, 52, 41), (122, 82, 74), (190, 88, 136), (214, 85, 113), (119, 42, 34), (67, 56, 52), (165, 83, 119), (208, 83, 113), (221, 127, 53), (211, 136, 143), (105, 36, 31), (204, 130, 95), (194, 119, 126), (101, 38, 31), (174, 163, 131), (221, 76, 143), (214, 67, 93), (190, 120, 84), (174, 94, 103), (97, 50, 42), (214, 207, 93), (211, 48, 127), (223, 56, 82), (199, 196, 103), (169, 98, 112), (244, 193, 75), (188, 63, 121), (202, 53, 75), (45, 74, 52), (154, 91, 99), (183, 131, 120), (209, 62, 142), (178, 52, 76), (164, 89, 96), (177, 119, 105), (189, 64, 140), (160, 35, 65), (119, 193, 218), (161, 102, 88), (216, 176, 117), (116, 50, 86), (157, 33, 61), (109, 51, 109), (158, 101, 94), (147, 90, 81), (152, 46, 64), (129, 105, 121), (118, 60, 58), (142, 78, 68), (189, 117, 67), (192, 109, 137), (183, 112, 152), (79, 34, 31), (165, 111, 67), (188, 101, 133), (28, 22, 24), (176, 41, 136), (185, 96, 128), (230, 53, 141), (137, 107, 105), (152, 110, 88), (166, 75, 106), (193, 41, 36), (232, 130, 178), (127, 86, 82), (207, 120, 100), (145, 89, 56), (161, 68, 97), (181, 38, 34), (134, 47, 38), (232, 143, 175), (206, 151, 146), (238, 149, 119), (216, 115, 145), (227, 109, 97), (219, 133, 158), (201, 143, 142), (233, 119, 92), (129, 202, 191), (210, 101, 140), (218, 57, 37), (244, 125, 165), (200, 135, 129), (217, 107, 72), (218, 95, 139), (174, 120, 110), (215, 78, 108), (187, 104, 96), (234, 119, 65), (210, 90, 135), (189, 122, 103), (218, 58, 84)]
NAMES_ORIGINAL = ['Twig Sunset Rose', 'Neon Orange', 'Breathing Fire', 'Love Weapon (Ltd. Ed.)', 'Cosmo', 'Morange', 'amnol', 'New York Apple', 'Crowned (Ltd Ed)', 'Runway Hit', 'Flamingo', 'Designer Blue', 'Lickable', 'Quaitzette', 'Prettv Boy', 'Matte Royal', 'Full Fuchsia', 'Back In Voque', 'Vledium Rare', 'Smoked Almond', 'Blue Beat', 'Pink Pigeon', 'Burnt Spice', 'Pure Happine', 'Red Brick Mulling Spices', 'So Chaud', 'Nico Kiss', 'Beetroot', 'Topped With Brandy', 'Little Buddha', 'Lady Danger', 'Toast And Butter', 'Sumac', 'Cafe Au Chic', 'Singer Ruse', 'Duzen Carnations Sweet Sakura', 'ghtly Charrer', 'Simply Smoked', 'Sunny Seoul', 'Dangerous', 'Pick Me Pick Mel', 'Fluid', 'EEss-Presso', 'Giddy', 'Brave Red, Cockney', 'Fleshpol', 'Galaxy Grey', 'Dark Side', 'Young Attitude', 'Fanfare', 'Dare You', 'The Entelope Please', '4Eva', 'Un And Un', 'Uniformly Fabulous', 'Fire Roasted Viva Glam', 'Blankety', 'Model Behavior', 'Apres Soiree', 'Fuchsia Flicker(Ltd Ed)', 'Politely Pink', 'Marsala', 'Viva Glam', 'Punk Couture', 'Tailored To Tease', 'Creme Gup', 'Half N Half', 'Paity Line', 'Oh, Lady', 'Skew', 'Velvet Teddy', 'Rocker', 'To Matte With Love', 'Fabby', 'Vegas Volt', 'Clouds In Mv Colfee', 'avenden Jade', 'Hang Up', 'Dance With Me', 'Mudesty', 'Tropic Tonic', 'Shv Girl', 'Viuletta', 'High Drama', 'Brave', 'Habanero', 'Hellebore', 'Pink-Off', 'Caviar', 'Please Me', 'Mangrove', 'Heroine', 'ovelorn', 'Faux , Fast Play', 'Lady Bug', 'Peachstock', 'Cyber', 'Pink Plaid', 'Gemz & Roses', 'Chili', 'Jubilee', 'Amorous', 'Retrograde (Ltd. Ed )', 'Patisserie', 'Dubonnet', 'Yash', 'Up the Amnp', 'Viva Glam', 'Silver Spoon (Ltd Ed)', 'Nippon', 'Cherish', "Tongue 'N' Chic", 'Amazed (Ltd Ed.)', 'See Sheer', 'Taupe', 'Rebel', 'Lustering', 'Buzzed Out (Ltd Ed )', 'Goral Bliss', 'Pure Zen', 'Apricot Gold', 'Noblesse', 'Impassioned', 'Metallic Rose', 'Gosta Chic', 'Ravishing', 'Strength', 'Instigator', 'Pink, You Think?', 'King Salmon', 'Prosperiti', 'Mocha', 'All Fired Up', 'Strawberry Torte', 'Crosswires', 'Peachy New Year', 'Touch', 'Beach Nut', 'Craving', 'Space Bubble', 'On Hold', 'Good Health', 'Persistence', 'awaii Ralt', 'Diva', 'Death By Chocolate', 'Paramount', 'Saint Germain', 'Fireworks', 'Kinda Sex', 'Double Fudge', 'Vlen Love Mystery', 'Goconut Macaroon', 'True Blood, MAC Red', 'Well Bred Brown', 'Antique Velvet', 'Smoked Purple', 'Creamy Peach Pie', 'Ruby Woo', 'Fresh Moroccan Nude Fudge', 'Twinkle', 'Brick-O-La', 'Brick Dust', 'Noon Noir', 'Pop Babe', 'Bombshell', 'Caramel Sugar', 'Del Rio', 'Retro', 'Stone', 'Soodbye Kiss', 'Gumball', 'Russian Red', 'Marrakesh', 'Bronx', 'Milan Mode(Ltd Ed )', 'Speak Louder', 'Spice It Upl', 'In My Fashion', 'Sweetie', 'Chatterbox', 'Banana Muffins', 'Peach Blossom', 'Studded Kiss , Dionysus', 'Rock', 'Plum Dandy', 'Sin', 'No Interruption', 'Candy Yum- Yum', 'Fusion Pink', 'Gilded Age', 'Mehr', 'Film Noir', 'Wild Extract', 'Ambrosial', 'Eros', 'Bey Lime Trifle', 'Syrup', ' Gold XIX!', 'Sirl About Town', 'Claretcast', 'Peace Love Unity , Respect', 'Capricious', 'Hug Mve', "Show Orchid'", 'Relentlessly Red', 'Creme in Your Coffee', 'Honevlove', 'Flat uut Fabulous', 'Cordovan', 'Wild Betry Frosting', 'Shrimpton, Spirit, Icon', 'Spolled Fabulous', 'Odyssey', 'Mittai Pink', "Queen's Violet", 'Midimauve', 'Verve', 'D For Danger', 'Sensory Overload', 'Viva Glam VI', 'Whirl', 'Bronze Shimmer', 'Snob', 'Purple Panna Cutta', 'Media', 'Naturally Transformed', 'Creme De La Femme', 'Stallion In The Spirit', 'Raspberry Creme', 'Hot Gossip', 'Raspberry Pavlova', 'Deep Rooted', 'Fresh Brew', 'Plumful', 'Fashion Legacy', 'Peally Gi', 'Viva Glam', 'Doe', 'Photo', 'Captive', 'Feels So Grand', 'carnivorous', 'Pave Bunn', 'Nothing To', "Bite O' Georgia", 'Star Magnolia', 'Rich & Restless', 'Strawbety Mousse', 'Really Me', 'Sushi Kiss', 'Galactic', 'Pink Nouveau', 'Quite The Standout', 'Electric Painbow', 'Driftwroud Babi Right (Ltd Ed.)', 'CB 96', 'Pink Peail Pop', '30 Me', 'Pink Trip', 'Shanghai Spice', 'Saigon Summe', 'Speed Dial', 'adybegood', 'Gumdrop']


def hex2rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def rgb2hex(rgb):
    return '#%02x%02x%02x' % rgb


def rgb2lab(rgb):
    return cs.cspace_convert(rgb, "sRGB255", "CIELab")


def topk_similar_colors(target_color_rgb, k=1):
    target_lab_color = rgb2lab(target_color_rgb)

    # Convert RGB colors to CIELAB
    # TODO: refactor this to precomputed these values of original_lab_colors
    original_lab_colors = []
    for color in RGB_ORIGINAL_COLORS:
        lab_color = rgb2lab(color)
        original_lab_colors.append(lab_color)

    original_lab_colors = np.array(original_lab_colors)

    # Calculate CIELAB color differences
    color_differences = np.linalg.norm(original_lab_colors - target_lab_color, axis=1)

    # Get the indices of the closest colors
    closest_indices = np.argsort(color_differences)[:k]

    # Get the top k most similar colors from the original_colors list
    similar_colors = {i: RGB_ORIGINAL_COLORS[i] for i in closest_indices}

    return similar_colors

def rgb_string_to_tuple(rgb_string):
    return ast.literal_eval(rgb_string)

def color_cells(val):
    if isinstance(val, str):
        rgb_tuple = rgb_string_to_tuple(val)
        # Convert RGB values to the 0-1 range
        rgb_normalized = [x / 255 for x in rgb_tuple]
        return f"background-color: {mcolors.to_hex(rgb_normalized)}"
    return ""

if __name__ == '__main__':

    # Sample target color in RGB
    target_color = (128, 128, 128)

    # Find the top 3 most similar colors to the target color
    k = 3
    similar_colors = topk_similar_colors(target_color, k)

    print("\nTarget RGB Color:", target_color)
    print(f"\nTop {k} Most Similar Colors:")
    for idx, lab_color in similar_colors.items():
        print(idx, lab_color)
