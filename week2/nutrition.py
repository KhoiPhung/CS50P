fruits = {
    "apple": "130",
    "avocado": "50",
    "sweet cherries": "100"
}

user_input = input("Input: ")

for fruit in fruits:
    if user_input == fruit:
        print("Calories:", fruits[fruit])
    else:
        pass



