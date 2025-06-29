from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        if output[1].lower() not in format:
            sys.exit("Invalid output")
        elif input[1].lower() != output[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            edit_photo(sys.argv[1], sys.argv[2])


def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()