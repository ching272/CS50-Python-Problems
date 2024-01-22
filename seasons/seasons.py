from datetime import date
import sys
import inflect
import operator

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    diff = operator.sub(date.today(), valid_date(dob))
    mins = diff.days * 24 * 60
    print(time_convert(mins))

def valid_date(d):
    try:
        return date.fromisoformat(d)
    except ValueError:
        sys.exit("Invalid date")

def time_convert(d):
    return p.number_to_words(d, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()
