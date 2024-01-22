def main():
    order()

def order():
    total = 0
    while True:
        try:
            item = input("Item: ").title()
            total = total + menu[item]
            print(f"Total: ${"{:.2f}".format(total)}")
        except KeyError:
            pass
        except EOFError:
            print()
            break

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()
