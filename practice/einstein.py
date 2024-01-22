def main():
    E_Cal()

def E_Cal():
    m = int(input("m: ").strip())
    E = m * pow(300000000, 2)
    print(f"E: {E}")

main()
