def main():
    text = input("Fraction: ")
    percentage = convert(text)
    fuel = gauge(percentage)
    print(fuel)


def convert(fraction):
    while True:
        try:
            #User input on fraction, splitting fraction by '/', then returning percentage
            numbers = text.split('/')
            x = int(numbers[0])
            y = int(numbers[1])

            fraction = (x/y) * 100

            if x > y:
                text = input("Fraction: ")

            return int(fraction)
        except (ValueError, ZeroDivisionError):
            raise ValueError
            raise ZeroDivisionError

def gauge(percentage):
    if percentage == 75:
        return "75%"
    elif percentage >= 50 and percentage <= 74:
        return "50%"
    elif percentage >= 25 and percentage <= 49:
        return "25%"
    elif percentage >= 76 and percentage <= 100:
        return "F"
    elif percentage >= 0 and percentage <= 24:
        return "E"


if __name__ == "__main__":
    main()