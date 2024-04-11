price = 50

while price > 0:
    print("Amount due:", price)
    coins = input("Insert coins: ")
    if int(coins) in [25, 10, 5]:
        price = int(price) - int(coins)
    else:
        pass

print("Change owded:", abs(price))