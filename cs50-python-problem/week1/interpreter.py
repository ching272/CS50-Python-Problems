exp = input("Expression: ").strip()

def cal(expr):
    li = expr.split(" ")
    x = int(li[0])
    y = li[1]
    z = int(li[2])
    
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z

print(round(float(cal(exp)),1))

