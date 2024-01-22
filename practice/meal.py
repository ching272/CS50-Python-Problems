def main():
    time = input("What time is it? ").strip().lower()
    convert(time)


def convert(time):
    if "." in time:
        tm, meridiem = time.split(" ")
        hour, mins = tm.split(":")
    else:
        meridiem = ""
        hour, mins = time.split(":")
    if meridiem == "p.m.":
        mer = 12
    else:
        mer = 0
    cnv_time = int(hour) + int(mins)/60 + mer
    if 7 <= cnv_time <= 8:
        print("breakfast time")
    elif 12 <= cnv_time <= 13:
        print("lunch time")
    elif 18 <= cnv_time <= 19:
        print("dinner time")


if __name__ == "__main__":
    main()
