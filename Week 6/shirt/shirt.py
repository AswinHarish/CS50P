from os import path
from PIL import Image, ImageOps
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if check_format(sys.argv[1], sys.argv[2]):
            add_images(sys.argv[1], sys.argv[2])


def check_format(infile, outfile):
    supported = [".jpg", ".jpeg", ".png"]

    fin = path.splitext(infile)[-1]
    fout = path.splitext(outfile)[-1]
    if fin not in supported:
        print(fin)
        sys.exit("Invalid input")
    elif fout not in supported:
        sys.exit("Invalid output")
    elif fin != fout:
        sys.exit("Input and output have different extensions")
    else:
        return True


def add_images(infile, outfile):
    try:
        shirt = Image.open("shirt.png", mode="r")
        size = shirt.size
        with Image.open(infile) as inf:
            resized_image = ImageOps.fit(inf, size)
            resized_image.paste(shirt, shirt)
            resized_image.save(outfile)

    except FileNotFoundError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
