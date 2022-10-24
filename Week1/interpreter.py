def main():
    user_input = input("Expression: ")
    x, y , z = user_input.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(float(x+z))
    elif y == "-":
        print(float(x-z))
    elif y == "*":
        print(float(x*z))
    elif y == "/":
        print(float(x/z))


main()