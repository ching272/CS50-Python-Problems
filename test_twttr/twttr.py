def main():
    str = input("Input: ").strip()
    print("Output:", shorten(str))


def shorten(word):
    result = ""
    for char in word:
        if char not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            result = result + char
    return result


if __name__ == "__main__":
    main()
