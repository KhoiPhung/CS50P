user_input = input("What is the answer to the great question of life? ")

match user_input:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
