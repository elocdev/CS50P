def main():
    greeting = input("Greeting: ")

    if "hello" in greeting.lower():
        print("$0")
    elif "h" == greeting.lower().strip()[0]:
        print("$20")
    else:
        print("$100")

main()
