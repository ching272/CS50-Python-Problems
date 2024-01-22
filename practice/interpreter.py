def main():
    math()

def math():
    expr = input("Expression: ").strip()
    x,y,z = expr.split(" ")
    n1 = int(x)
    n2 = int(z)
    match y:
        case "+":
            print(round(float(n1+n2), 1))
        case "-":
            print(round(float(n1-n2), 1))
        case "*":
            print(round(float(n1*n2), 1))
        case "/":
            print(round(float(n1/n2), 1))

main()

