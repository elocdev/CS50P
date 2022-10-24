menu_items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main ():
    total_price = 0
    
    while True: 
        try:
            order = input("Item: ")
            order = order.title()
            
            for i in menu_items:
                if order == i:
                    total_price += menu_items[i]
                    print("Total: $" + str(total_price) + "0")
                else:
                    continue
        except EOFError:
            print("\n")
            break
        else:
            continue
            
    
main()