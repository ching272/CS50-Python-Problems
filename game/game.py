import random

def main():
    guess(level())

def level():
    while True:
        try:
            lv = int(input("Level: ").strip())
            if lv > 0:
                return random.randint(1, lv)
        except ValueError:
            pass

def guess(num):
    while True:
        try:
            ans = int(input("Guess: ").strip())
            if ans > num:
                print("Too large!")
            elif ans < num:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
