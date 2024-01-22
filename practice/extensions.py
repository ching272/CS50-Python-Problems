def main():
    file()

def file():
    name = input("File name: ").strip()
    name_li = name.split(".")
    ext = name_li[-1].lower()
    match ext:
        case "gif" | "png":
            print("image/" + ext)
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print("application/" + ext)
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

main()
