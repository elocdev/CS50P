def main():
    gauge = fuel();
    if gauge >= 0.25 and gauge <= 0.75:
        text = round(gauge*100)
        print(f"{text}%")
    elif gauge >= 0.76 and gauge <= 1.00:
        print("F")
    elif gauge >= 0 and gauge <= 0.24:
        print("E")


def fuel():
    while True:
        try:
            #User input on fraction, splitting fraction by '/', then returning percentage
            text =  input("Fraction: ")
            numbers = text.split('/')
            x = int(numbers[0])
            y = int(numbers[1])
            result = x / y

            if x > y:
                text = input("Fraction: ")

            return result

        #Checks for ValueError and Zero Division
        except (ValueError, ZeroDivisionError):
            text = input("Fraction: ")
        else:
            return result


main()