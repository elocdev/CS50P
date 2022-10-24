grocery_list = []
num_of_items = {}

while True:
    try:
        #Asks user for input
        #Makes all items uppercase
        #Appends item into grocery list array
        #Sorts the grocery list
        #Continues asking user until EOFError
        grocery_item = input("")
        grocery_item = grocery_item.upper()
        
        grocery_list.append(grocery_item)
        grocery_list.sort()
    
    except EOFError:
        #For every item in grocery list
        #If the item appears in dict of num of items
        #Else add that item to the dictionary of items
        for item in grocery_list:
            if item in num_of_items:
                num_of_items[item] += 1
            else:
                num_of_items[item] = 1
        #Printing out the items in the dictionary of items
        for x in num_of_items:
            print(str(num_of_items[x]) + " " + x)
        break
    else:
        continue