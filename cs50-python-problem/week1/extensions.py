flnm = input("File name: ").strip().lower()

#To get the suffix
def suf(str):
    if "." in str:
        lst = str.split(".")
        return lst[len(lst) - 1]
    else:
        return ""

match suf(flnm):
    case "gif" | "png":
        print("image/" + suf(flnm))
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + suf(flnm))
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")

