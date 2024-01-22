import json
import requests
import sys


def main():
    result = round(bit_num()*bit_price(), 4)
    print(f"${result:,.4f}")

#Get the number of Bitcoins
def bit_num():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        if float(sys.argv[1]):
            return float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

#Get the current price of Bitcoins
def bit_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    p = response.json()
    return p["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()




