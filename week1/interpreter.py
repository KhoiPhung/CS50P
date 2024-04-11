expression = input("Expression: ")

#splitting the input into x, y and z

x, y, z = expression.split(" ")

match y:
    case "+":
        print(f"{float(int(x) + int(z)):.1f}")
    case "-":
        print(f"{float(int(x) - int(z)):.1f}")
    case "*":
        print(f"{float(int(x) * int(z)):.1f}")
    case "/":
        print(f"{float(int(x) / int(z)):.1f}")

