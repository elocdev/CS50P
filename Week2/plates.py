def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #Min of 2 characters, Max of 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    #Checking first two characters letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    #Checking numbers in the middle
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    #Check no periods, spaces, punctuations
    for letter in s:
        if letter in ['.', ',', '!', '?', ' ']:
            return False

    return True

main()
