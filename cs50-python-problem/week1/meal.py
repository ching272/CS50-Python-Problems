def main():
    tm = input("What time is it? ").strip()

    if 7.00 <= convert(tm) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(tm) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(tm) <= 19.00:
        print("dinner time")


def convert(time):
    #To get the hour, the min and the meridiem
    mertime = 0
    if " " in time:
        ltm  = time.split(" ")
        hour, min = ltm[0].split(":")
        if ltm[1] == "p.m.":
            mertime = 12
    else:
        hour, min = time.split(":")

    return round(float(int(hour) + int(min)/60 + mertime),2)


if __name__ == "__main__":
    main()
