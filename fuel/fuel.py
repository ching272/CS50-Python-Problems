def main():
    result = int(fuel()*100)
    if result >= 99:
        print("F")
    elif result > 1:
        print(f"{result}%")
    else:
        print("E")

def fuel():
    while True:
        try:
            str = input("Fractions: ").split("/")
            indicate = round(int(str[0]) / int(str[1]),2)
            if indicate <= 1:
                return indicate
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


main()
