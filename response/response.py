from validator_collection import validators, checkers

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        result = checkers.is_email(s)
        return "Valid" if result else "Invalid"
    except ValueError:
        return "Invalid"



if __name__ == "__main__":
    main()
