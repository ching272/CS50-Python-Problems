import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    am_check = "([1-9]|1[0-2])(:[0-5][0-9])? AM"
    pm_check = "([1-9]|1[0-2])(:[0-5][0-9])? PM"
    if re.search(am_check+" to "+pm_check, s.strip()) or re.search(pm_check+" to "+am_check, s.strip()):
        start, end = s.split(" to ")
        return hour_convert(start)+" to "+hour_convert(end)
    else:
        raise ValueError


def hour_convert(s):
    time, ind = s.strip().split(" ")
    #add minutes
    if ":" in time:
        hour, min = time.split(":")
        if len(min) == 1:
            min = "0"+min
    else:
        hour = time
        min = "00"
    #convert_am_hour
    if ind == "AM":
        if len(hour) == 1:
            hour = "0"+hour
        return hour.replace("12", "00")+":"+min
    #convert_pm_hour
    else:
        hour = str(int(hour) + 12)
        return hour.replace("24", "12")+":"+min

if __name__ == "__main__":
    main()



