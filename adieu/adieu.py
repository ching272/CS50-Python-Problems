import inflect

p = inflect.engine()

def main():
    print("Adieu, adieu, to", p.join(names()))

def names():
    name_list = []
    while True:
        try:
            name = input("Name: ").strip().title()
            name_list.append(name)
        except EOFError:
            break
    return name_list

if __name__ == "__main__":
    main()

