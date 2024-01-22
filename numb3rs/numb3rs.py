import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$", ip):
        id = True
        nums = list(map(int, matches.groups()))
        for i in nums:
            if i > 255:
                id = False
                break
    else:
        id = False
    return id


if __name__ == "__main__":
    main()
