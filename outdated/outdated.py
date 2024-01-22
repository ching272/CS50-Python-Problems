def main():
    trans()

def trans():
    while True:
        date = input("Date: ").strip()
        try:
            if date.find(",") != -1:
                month, day, year = date.replace(",","").split(" ")
                mth = int(months.index(month)+1)
            else:
                mth, day, year = date.split("/")
            if 0 < int(day) < 32 and 0 < int(mth) < 13:
                print(f"{year}-{int(mth):02}-{int(day):02}")
                break
        except:
            pass

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

main()

