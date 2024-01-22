def main():
    print("Amount Due: 50")
    coin()

def coin():
    total_coin = 0
    while total_coin < 50:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            total_coin = total_coin + coin
        if total_coin >= 50:
            print("Change Owed:", total_coin - 50)
        else:
            print("Amount Due:", 50 - total_coin)


main()




