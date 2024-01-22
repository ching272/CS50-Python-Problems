def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return len_check(s) and s[0:2].isalpha() and s[2:7].isalnum() and last_cha(s) and start_num(s) and al_in_num(s)

#To check the len
def len_check(s):
    return True if 2 <= len(s) <= 6 else False


#To check number not in the middle
def last_cha(s):
    result = True
    if s[len(s)-1].isalpha():
        for i in s:
            if i.isnumeric():
                result = False
                break
    return result

#To check the first num is not 0
def start_num(s):
    num_li = []
    for i in s:
        if i.isnumeric():
            num_li.append(i)
    if len(num_li) > 0:
        return num_li[0] != "0"
    else:
        return True

def al_in_num(s):
    for i in s:
        if i.isnumeric():
            num_str = s[s.find(i):len(s)]
            break
    return True if s.isalpha() else num_str.isnumeric()

if __name__ == "__main__":
    main()
