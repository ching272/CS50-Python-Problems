import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"src=\"https?://(www\.)?youtube\.com/embed/(.+)\"", s, re.IGNORECASE):
        link = match.group(2)
        return f"https://youtu.be/{link}"
    else:
        return "None"

if __name__ == "__main__":
    main()
