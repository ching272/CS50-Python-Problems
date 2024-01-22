import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        while True:
            try:
                with open(f"{sys.argv[1]}") as file:
                    reader = csv.DictReader(file)
                    with open(f"{sys.argv[2]}", "w") as sfile:
                        writer = csv.DictWriter(sfile, fieldnames=["first", "last", "house"])
                        writer.writeheader()
                        for row in reader:
                            writer.writerow({"first": row["name"].split(",")[1].strip(), "last": row["name"].split(",")[0].strip(), "house": row["house"]})
                    break
            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
