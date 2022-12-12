# Create a program that converts regular images into ascii-art.

# Start by loading an image into memory. Check its dimensions and for each pixel, find the red, green and blue value of each pixel.
# Find the average and take its corresponding ASCII character. 

from PIL import Image
from sys import argv

ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def main():
    before = Image.open(argv[1])

    ascii_art = info_receiver(before)
    save_to_file(ascii_art)

    #print(ascii_art)

def info_receiver(image):
    ascii_art = []

    width = image.width
    height = image.height
    
    #print(f"Height is {height} and width is {width}.")

    for y in range(height):
        line = ''
        for x in range(width):
            pixel = image.getpixel((x, y))
            #print(pixel)
            line += pixel_to_ascii(pixel)
            #print(line)
        ascii_art.append(line)

    return ascii_art


def pixel_to_ascii(pixel):
    value = int((pixel[0] + pixel[1] + pixel[2]) / len(ascii_characters))
    #print(value)
    return ascii_characters[value]


def save_to_file(ascii_art):
    with open("ascii_art.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write("\n")
    return

if __name__ == "__main__":
    main()
