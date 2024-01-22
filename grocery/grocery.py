def main():
    grocery_list()

def grocery_list():
    list = {}
    while True:
        try:
            item = input().upper()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            result = sorted(list)
            for i in result:
                print(list[i],i)
            break


main()
