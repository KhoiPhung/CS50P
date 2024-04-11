def convert(input):
    converted_input = input.replace(":)", "🙂").replace(":(", "🙁")
    return converted_input

def main():
    user_input = input()
    new_input = convert(user_input)
    print(new_input)

main()