from PIL import Image

MAX_INTENSITY = 255
SCALE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_pixel_matrix(img, height, width):
    pixel_matrix = []

    pixels = img.load()
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        pixel_matrix.append(row)
    
    return pixel_matrix

def get_intensity_matrix(pixel_matrix):
    intensity_matrix = []
    
    for row in pixel_matrix:
        new_row = []
        for pixel in row:
            R, G, B = pixel
            mono = int((R+G+B)/3)
            new_row.append(mono)
        intensity_matrix.append(new_row) 
    
    return intensity_matrix

def get_char_matrix(intensity_matrix):
    char_matrix = []
    
    for row in intensity_matrix:
        new_row = []
        for pixel_intensity in row:
            char = convert_to_char(pixel_intensity)
            new_row.append(char)
        char_matrix.append(new_row)
    
    return char_matrix

def convert_to_char(pixel_intensity):
    global SCALE, MAX_INTENSITY
    idx = int(pixel_intensity / MAX_INTENSITY * (len(SCALE)-1))
    return SCALE[idx]

if __name__ == "__main__":
    try:
        # load file
        filepath = "images/rick.jpg"
        img = Image.open(filepath)

        # reduce image size
        img.thumbnail((1000, 350))
        width, height = img.size

        # convert image to a pixel matrix of size height x width, where each pixel is 
        # a tuple of rgb values
        pixel_matrix = get_pixel_matrix(img, height, width)

        # transform pixel matrix to represent each pixel using a single number instead of a tuple
        intensity_matrix = get_intensity_matrix(pixel_matrix)

        # create char matrix assigning each pixel an ascii character based on its intensity
        char_matrix = get_char_matrix(intensity_matrix)
        
        # print ascii image
        for row in char_matrix:
            # each char in row is multiplied by 3 as the height of a char in terminal is
            # 3 times its width
            print("".join([c*3 for c in row]))
    
    except FileNotFoundError:
        print("Couldn't locate file.")