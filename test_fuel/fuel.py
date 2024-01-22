def main():
    while True:
        inp = input("Fraction: ").strip()
        try:
            fraction = convert(inp)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(fraction))

def convert(fraction):
    x,y = fraction.split("/")
    if x.isnumeric() and y.isnumeric():
        if int(y) == 0:
            raise ZeroDivisionError
        elif int(x) < int(y):
            return round(int(x)/int(y)*100)
        else:
            raise ValueError
    else:
        raise ValueError

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage > 1:
        return f"{percentage}%"
    else:
        return "E"


if __name__ == "__main__":
    main()
