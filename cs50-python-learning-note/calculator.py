x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")




#==========================================
def main():
    a = int(input("What's a? "))
    print("a square is", square(a))

def square(num):
    return num**2 #or num*num or pow(num,2)

main()
