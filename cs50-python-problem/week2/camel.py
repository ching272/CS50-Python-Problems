def main():
    str = input("camelCase: ").strip()
    to_snake(str)
    print()



def to_snake(str):
    li = list(str)
    for i in range(len(li)):
        if 65 <= ord(li[i]) <=90:
            li[i] = "_" + li[i].lower()

    print("snake_case: ", end = "")
    for i in li:
        print(i, end="")



main()
