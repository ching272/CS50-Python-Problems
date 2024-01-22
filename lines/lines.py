import sys

def LOC(name):
    count = 0
    if name.find(".py") == -1:
        sys.exit("Not a Python file")
    else:
        while True:
            try:
                with open(f"{name}", "r") as file:
                    for lines in file:
                        if lines.strip() != "" and not lines.strip().startswith("#"):
                            count = count + 1
                return count
            except FileNotFoundError:
                sys.exit("File does not exist")


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        print(LOC(sys.argv[1]))


if __name__ == "__main__":
    main()
