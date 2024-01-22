import re
import sys


def main():
    print(count(input("Input: ")))


def count(s):
    matches = []
    str = r"(^u| u)(m$|m\W)"
    matches = re.findall(str, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
