import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].find(".csv") == -1:
            sys.exit("Not a CSV file")
        else:
            while True:
                try:
                    table = []
                    with open(f"{sys.argv[1]}") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            table.append(row)
                        print(tabulate(table[1:], table[0], tablefmt="grid"))
                    break
                except FileNotFoundError:
                    sys.exit("File does not exist")


if __name__ == "__main__":
    main()
