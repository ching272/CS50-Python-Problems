def main():
    emo()

def emo():
    inp = input("").strip()
    print(inp.replace(":)", "🙂").replace(":(", "🙁"))

main()
