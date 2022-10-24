def convert(input):
    #happy face conversion
    msg1 = input.replace(":)", "🙂")

    #sad face conversion
    msg2 = msg1.replace(":(", "🙁")

    return msg2

def main():
    msg = convert(input())
    print(msg)

main()