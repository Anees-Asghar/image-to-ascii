import sys
from PIL import Image


MAX_INTENSITY = 255
INTENSITY_SCALE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def get_pixel_matrix(img, height, width):
    """
        Return a pixel matrix of size height x width from the image provided, where each pixel is 
        a tuple of rgb values.
    """
    pixel_matrix = []

    pixels = img.load()
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        pixel_matrix.append(row)
    
    return pixel_matrix


def get_intensity_matrix(pixel_matrix):
    """
        Return an intensity matrix provided a pixel matrix, where the intensity of a pixel is the 
        average of its rgb values.
    """
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
    """
        Return a character matrix provided an intensity matrix, where each pixel is assigned a 
        character from the INTENSITY_SCALE based on its intensity.
    """
    char_matrix = []
    
    for row in intensity_matrix:
        new_row = []
        for pixel_intensity in row:
            char = convert_to_char(pixel_intensity)
            new_row.append(char)
        char_matrix.append(new_row)
    
    return char_matrix


def convert_to_char(pixel_intensity):
    """
        Return a character from the INTENSITY_SCALE based on the pixel_intensity provided.
    """
    idx = int(pixel_intensity / MAX_INTENSITY * (len(INTENSITY_SCALE)-1))
    return INTENSITY_SCALE[idx]


def render_art(char_matrix):
    """
        Print the ASCII art on the terminal window provided the character matrix.
    """
    for row in char_matrix:
        # the height of a character on a terminal window is roughly 3 times its width, to offset
        # this we print each character of each row of char_matrix 3 times
        modified_row = [c*3 for c in row]
        print("".join(modified_row))


def main():
    try:
        # check if filename has been provided
        if len(sys.argv) == 1:
            print("Please provide a filename. For example\n\tpython main.py pups.jpg")
            return

        # load file
        filepath = f"images/{sys.argv[1]}"
        img = Image.open(filepath)

        # reduce image size
        img.thumbnail((1000, 200))
        width, height = img.size

        # get pixel matrix from image
        pixel_matrix = get_pixel_matrix(img, height, width)

        # get intensity matrix from pixel matrix
        intensity_matrix = get_intensity_matrix(pixel_matrix)

        # get character matrix from intensity matrix
        char_matrix = get_char_matrix(intensity_matrix)
        
        # print ascii art
        render_art(char_matrix)
    
    except FileNotFoundError:
        print(f"Couldn't find {sys.argv[1]} in the images folder.")


if __name__ == "__main__":
    main()
