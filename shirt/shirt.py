import sys
import os
from PIL import Image, ImageOps

def path_check(file):
    return ".jpg" in file or ".jpeg" in file or ".png" in file

def main():
    img_paths = [".jpg", ".jpeg", ".png"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        before = sys.argv[1].strip().lower()
        after = sys.argv[2].strip().lower()
        if path_check(before) and path_check(after):
            before_path = os.path.splitext(before)[1]
            after_path = os.path.splitext(after)[1]
            if before_path != after_path:
                sys.exit("Input and output have different extensions")
            else:
                while True:
                    try:
                        with Image.open(before) as img:
                            shirt = Image.open("shirt.png")
                            img_crop = ImageOps.fit(img, shirt.size)
                            img_crop.paste(shirt, mask = shirt)
                            return img_crop.save(after)
                    except FileNotFoundError:
                        sys.exit("Input does not exist")
        else:
            sys.exit("Invalid input")


if __name__ == "__main__":
    main()

