grocery_list = {}


while True:
    try:
        key = input()
        if key in grocery_list:
            grocery_list[key] += 1
        else:
            grocery_list[key] = 1
    except EOFError:
        for key, value in grocery_list.items():
            print(f"{value} {key.upper()}")
        break



