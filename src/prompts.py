
ZERO_SHOT_PROMPT_TEMPLATE = """
As a head of MAC cosmetic advertisement department and marketing expert,
I want to create a lipstick name that is based on the following RGB tuple color delimited by triple quotes
\"\"\"{color}\"\"\"
and follows the MAC cosmetics name style for lipstick and is easy to remember.
Give your answer with only the generated lipstick name without any punctuation.
"""

FEW_SHOT_PROMPT_TEMPLATE = """
As a head of MAC cosmetic advertisement department and marketing expert,
Create only one lipstick name that is based on the pairs of RGB tuples color and lipstick name delimited by
<hex> and <name> tags below:

{examples}
<rgb>{color}<rgb>,

do not repeat any name from the examples
output only the new name between the <name> tag without the tag or any punctuation
"""

MANY_SHOT_PROMPT_TEMPLATE = """
As a head of MAC cosmetic advertisement department and marketing expert
Create only one lipstick name that is based on the pairs of RGB tuples color and lipstick name delimited by
<hex> and <name> tags below do not repeat any name from the examples and the output should only contain the name inside the <name> tag

<rgb>(173, 94, 89)<rgb>, <name>Twig Sunset Rose<name>
<rgb>(236, 94, 58)<rgb>, <name>Neon Orange<name>
<rgb>(210, 87, 141)<rgb>, <name>Breathing Fire<name>
<rgb>(130, 26, 27)<rgb>, <name>Love Weapon (Ltd. Ed.)<name>
<rgb>(176, 98, 96)<rgb>, <name>Cosmo<name>
<rgb>(228, 88, 53)<rgb>, <name>Morange<name>
<rgb>(118, 199, 242)<rgb>, <name>amnol<name>
<rgb>(183, 70, 116)<rgb>, <name>New York Apple<name>
<rgb>(72, 28, 25)<rgb>, <name>Crowned (Ltd Ed)<name>
<rgb>(185, 80, 76)<rgb>, <name>Runway Hit<name>
<rgb>(213, 89, 65)<rgb>, <name>Flamingo<name>
<rgb>(52, 97, 180)<rgb>, <name>Designer Blue<name>
<rgb>(194, 60, 110)<rgb>, <name>Lickable<name>
<rgb>(103, 28, 59)<rgb>, <name>Beetroot<name>
<rgb>(159, 95, 85)<rgb>, <name>Topped With Brandy<name>
<rgb>(229, 132, 141)<rgb>, <name>Little Buddha<name>
<rgb>(197, 58, 53)<rgb>, <name>Lady Danger<name>
<rgb>(179, 85, 60)<rgb>, <name>Toast And Butter<name>
<rgb>(61, 30, 45)<rgb>, <name>Sumac<name>
<rgb>(190, 144, 121)<rgb>, <name>Cafe Au Chic<name>
<rgb>(215, 124, 133)<rgb>, <name>Singer Ruse<name>
<rgb>(196, 53, 45)<rgb>, <name>Duzen Carnations Sweet Sakura<name>
<rgb>(167, 154, 174)<rgb>, <name>ghtly Charrer<name>
<rgb>(154, 125, 111)<rgb>, <name>Simply Smoked<name>
<rgb>(208, 113, 119)<rgb>, <name>Sunny Seoul<name>
<rgb>(180, 46, 37)<rgb>, <name>Dangerous<name>
<rgb>(144, 113, 154)<rgb>, <name>Pick Me Pick Mel<name>
<rgb>(111, 44, 62)<rgb>, <name>Fluid<name>
<rgb>(139, 106, 89)<rgb>, <name>EEss-Presso<name>
<rgb>(204, 104, 116)<rgb>, <name>Giddy<name>
<rgb>(219, 162, 145)<rgb>, <name>Fleshpol<name>
<rgb>(133, 106, 137)<rgb>, <name>Galaxy Grey<name>
<rgb>(95, 31, 48)<rgb>, <name>Dark Side<name>
<rgb>(23, 59, 71)<rgb>, <name>Young Attitude<name>
<rgb>(199, 94, 108)<rgb>, <name>Fanfare<name>
<rgb>(151, 43, 40)<rgb>, <name>Dare You<name>
<rgb>(202, 151, 132)<rgb>, <name>The Entelope Please<name>
<rgb>(158, 118, 181)<rgb>, <name>4Eva<name>
<rgb>(75, 40, 62)<rgb>, <name>Uniformly Fabulous<name>
<rgb>(149, 30, 24)<rgb>, <name>Fire Roasted Viva Glam<name>
<rgb>(195, 132, 117)<rgb>, <name>Blankety<name>
<rgb>(114, 62, 147)<rgb>, <name>Model Behavior<name>
<rgb>(60, 20, 29)<rgb>, <name>Apres Soiree<name>
<rgb>(225, 71, 167)<rgb>, <name>Fuchsia Flicker(Ltd Ed)<name>
<rgb>(218, 158, 158)<rgb>, <name>Politely Pink<name>
<rgb>(134, 39, 35)<rgb>, <name>Marsala<name>
<rgb>(195, 127, 116)<rgb>, <name>Viva Glam<name>
<rgb>(75, 38, 90)<rgb>, <name>Punk Couture<name>
<rgb>(165, 49, 110)<rgb>, <name>Tailored To Tease<name>
<rgb>(226, 150, 152)<rgb>, <name>Creme Gup<name>
<rgb>(199, 131, 112)<rgb>, <name>Half N Half<name>
<rgb>(120, 37, 57)<rgb>, <name>Paity Line<name>
<rgb>(98, 20, 59)<rgb>, <name>Oh, Lady<name>
<rgb>(218, 138, 139)<rgb>, <name>Skew<name>
<rgb>(198, 127, 109)<rgb>, <name>Velvet Teddy<name>
<rgb>(120, 33, 42)<rgb>, <name>Rocker<name>
<rgb>(173, 56, 85)<rgb>, <name>To Matte With Love<name>
<rgb>(209, 137, 138)<rgb>, <name>Fabby<name>
<rgb>(215, 88, 82)<rgb>, <name>Vegas Volt<name>
<rgb>(215, 143, 121)<rgb>, <name>Clouds In Mv Colfee<name>
<rgb>(215, 124, 217)<rgb>, <name>avenden Jade<name>
<rgb>(79, 25, 36)<rgb>, <name>Hang Up<name>
<rgb>(154, 31, 49)<rgb>, <name>Dance With Me<name>
<rgb>(187, 121, 123)<rgb>, <name>Mudesty<name>
<rgb>(217, 81, 69)<rgb>, <name>Tropic Tonic<name>
<rgb>(221, 139, 115)<rgb>, <name>Shv Girl<name>
<rgb>(158, 50, 172)<rgb>, <name>Viuletta<name>
<rgb>(82, 29, 37)<rgb>, <name>High Drama<name>
<rgb>(187, 108, 114)<rgb>, <name>Brave<name>
<rgb>(228, 68, 52)<rgb>, <name>Habanero<name>
<rgb>(135, 50, 135)<rgb>, <name>Hellebore<name>
<rgb>(218, 156, 171)<rgb>, <name>Pink-Off<name>
<rgb>(40, 34, 34)<rgb>, <name>Caviar<name>
<rgb>(183, 97, 100)<rgb>, <name>Please Me<name>
<rgb>(234, 51, 37)<rgb>, <name>Mangrove<name>
<rgb>(117, 55, 122)<rgb>, <name>Heroine<name>
<rgb>(198, 55, 38)<rgb>, <name>Lady Bug<name>
<rgb>(196, 133, 98)<rgb>, <name>Peachstock<name>
<rgb>(63, 37, 64)<rgb>, <name>Cyber<name>
<rgb>(192, 101, 119)<rgb>, <name>Pink Plaid<name>
<rgb>(190, 94, 98)<rgb>, <name>Gemz & Roses<name>
<rgb>(164, 62, 50)<rgb>, <name>Chili<name>
<rgb>(180, 124, 101)<rgb>, <name>Jubilee<name>
<rgb>(164, 76, 92)<rgb>, <name>Amorous<name>
<rgb>(180, 47, 48)<rgb>, <name>Retrograde (Ltd. Ed )<name>
<rgb>(208, 118, 118)<rgb>, <name>Patisserie<name>
<rgb>(151, 47, 38)<rgb>, <name>Dubonnet<name>
<rgb>(174, 117, 90)<rgb>, <name>Yash<name>
<rgb>(165, 77, 151)<rgb>, <name>Up the Amnp<name>
<rgb>(131, 55, 65)<rgb>, <name>Viva Glam<name>
<rgb>(74, 70, 87)<rgb>, <name>Silver Spoon (Ltd Ed)<name>
<rgb>(203, 115, 113)<rgb>, <name>Nippon<name>
<rgb>(171, 109, 84)<rgb>, <name>Cherish<name>
<rgb>(130, 42, 103)<rgb>, <name>Tongue 'N' Chic<name>
<rgb>(136, 46, 120)<rgb>, <name>Amazed (Ltd Ed.)<name>
<rgb>(211, 112, 106)<rgb>, <name>See Sheer<name>
<rgb>(154, 91, 73)<rgb>, <name>Taupe<name>
<rgb>(89, 31, 71)<rgb>, <name>Rebel<name>
<rgb>(221, 75, 122)<rgb>, <name>Lustering<name>
<rgb>(215, 67, 115)<rgb>, <name>Buzzed Out (Ltd Ed )<name>
<rgb>(239, 133, 133)<rgb>, <name>Goral Bliss<name>
<rgb>(225, 149, 133)<rgb>, <name>Pure Zen<name>
<rgb>(168, 97, 79)<rgb>, <name>Apricot Gold<name>
<rgb>(73, 29, 62)<rgb>, <name>Noblesse<name>
<rgb>(218, 73, 116)<rgb>, <name>Impassioned<name>
<rgb>(192, 90, 111)<rgb>, <name>Metallic Rose<name>
<rgb>(176, 129, 161)<rgb>, <name>Beach Nut<name>
<rgb>(180, 56, 82)<rgb>, <name>Craving<name>
<rgb>(128, 52, 62)<rgb>, <name>Space Bubble<name>
<rgb>(205, 80, 86)<rgb>, <name>On Hold<name>
<rgb>(202, 94, 82)<rgb>, <name>Good Health<name>
<rgb>(139, 78, 59)<rgb>, <name>Persistence<name>
<rgb>(205, 140, 183)<rgb>, <name>awaii Ralt<name>
<rgb>(153, 51, 75)<rgb>, <name>Diva<name>
<rgb>(111, 41, 43)<rgb>, <name>Death By Chocolate<name>
<rgb>(151, 75, 59)<rgb>, <name>Paramount<name>
<rgb>(216, 106, 179)<rgb>, <name>Saint Germain<name>
<rgb>(229, 49, 48)<rgb>, <name>Fireworks<name>
<rgb>(208, 129, 114)<rgb>, <name>Kinda Sex<name>
<rgb>(88, 36, 23)<rgb>, <name>Double Fudge<name>
<rgb>(150, 77, 123)<rgb>, <name>Vlen Love Mystery<name>
<rgb>(221, 167, 141)<rgb>, <name>Goconut Macaroon<name>
<rgb>(191, 39, 34)<rgb>, <name>True Blood, MAC Red<name>
<rgb>(181, 102, 87)<rgb>, <name>Well Bred Brown<name>
<rgb>(66, 28, 15)<rgb>, <name>Antique Velvet<name>
<rgb>(65, 32, 53)<rgb>, <name>Smoked Purple<name>
<rgb>(230, 135, 117)<rgb>, <name>Creamy Peach Pie<name>
<rgb>(179, 39, 40)<rgb>, <name>Ruby Woo<name>
<rgb>(157, 83, 74)<rgb>, <name>Fresh Moroccan Nude Fudge<name>
<rgb>(233, 138, 94)<rgb>, <name>Twinkle<name>
<rgb>(189, 61, 61)<rgb>, <name>Brick-O-La<name>
<rgb>(145, 71, 62)<rgb>, <name>Brick Dust<name>
<rgb>(155, 125, 117)<rgb>, <name>Noon Noir<name>
<rgb>(205, 91, 150)<rgb>, <name>Pop Babe<name>
<rgb>(217, 109, 135)<rgb>, <name>Bombshell<name>
<rgb>(110, 52, 30)<rgb>, <name>Caramel Sugar<name>
<rgb>(170, 60, 63)<rgb>, <name>Del Rio<name>
<rgb>(139, 62, 52)<rgb>, <name>Retro<name>
<rgb>(134, 96, 85)<rgb>, <name>Stone<name>
<rgb>(196, 99, 144)<rgb>, <name>Soodbye Kiss<name>
<rgb>(233, 102, 134)<rgb>, <name>Gumball<name>
<rgb>(162, 46, 47)<rgb>, <name>Russian Red<name>
<rgb>(134, 52, 41)<rgb>, <name>Marrakesh<name>
<rgb>(122, 82, 74)<rgb>, <name>Bronx<name>
<rgb>(190, 88, 136)<rgb>, <name>Milan Mode(Ltd Ed )<name>
<rgb>(214, 85, 113)<rgb>, <name>Speak Louder<name>
<rgb>(119, 42, 34)<rgb>, <name>Spice It Upl<name>
<rgb>(67, 56, 52)<rgb>, <name>In My Fashion<name>
<rgb>(165, 83, 119)<rgb>, <name>Sweetie<name>
<rgb>(208, 83, 113)<rgb>, <name>Chatterbox<name>
<rgb>(221, 127, 53)<rgb>, <name>Banana Muffins<name>
<rgb>(211, 136, 143)<rgb>, <name>Peach Blossom<name>
<rgb>(105, 36, 31)<rgb>, <name>Studded Kiss , Dionysus<name>
<rgb>(204, 130, 95)<rgb>, <name>Rock<name>
<rgb>{color}<rgb>,
"""

IMAGE_DESCRIPTION_PROMPT = """
Your task is to create a prompt for a generative ai to create an image for a lipstick ad with no text using the Mac Cosmetic aesthetic based on the lipstick RGB color and name which are {color} and {name}

The generated prompt should follow the below rules to help you build this prompt:

the image should not contain any writing on it.
the image background color needs to be on contrast and tone with the rgb color {color}
the look and feel of the image should match with the lipstick name {name}
the image should have a "Flat lighting" mood
the prompt should define a landscape, style, color and subject based on the RGB color and lipstick name provided
the prompt should use the words Photorealistic, Product photography, Cosmetic Product
The prompt should have a maximum of 300 characters
"""

IMAGE_AD_PROMPT = """
Generative AI, create a photorealistic, product photography image of a LIPSTICK named {name} with the RGB color {color} as the main color,
flat lighting, and a landscape, style, subject that reflects the lipstick name and the image should not contain any words or letters on it.
"""
