import random


def main():
    correct = 0
    level = get_level()
    for _ in range(1, 11):
        fail = 0
        x = generate_integer(level)
        y = generate_integer(level)
        ans = int(x + y)
        while fail < 3:
            while True:
                try:
                    rep = int(input(f"{x} + {y} = "))
                    break
                except ValueError:
                    pass
            if rep == ans:
                correct += 1
                break
            else:
                print("EEE")
                fail += 1
            if fail == 3:
                print(f"{x} + {y} = {ans}")
    print(f"Score: {correct}")



def get_level():
    while True:
        try:
            lv = int(input("Level: "))
            if 0 < lv <4:
                return lv
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1 ), 10 ** level - 1)


if __name__ == "__main__":
    main()
