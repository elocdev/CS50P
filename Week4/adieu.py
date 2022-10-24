import inflect
import sys

p = inflect.engine()

names_list = []

while True:
    try:
        names = input("Name: ").title()
        if len(names) < 1:
            sys.exit()
        
        names_list.append(names)
        output = p.join(names_list)
    
    except EOFError:
        print("\n")
        print("Adieu, adieu, to " + output)
        break
    
    else:
        continue