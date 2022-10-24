coke_price = 50

while coke_price > 0:
    print("Amount Due: ", coke_price)
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        coke_price -= insert_coin

change_owed = abs(coke_price)
print("Change Owed: ", change_owed)