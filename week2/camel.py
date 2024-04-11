def main():
    camel_name = input("camelCase: ")
    print(camel_to_snake(camel_name))

def camel_to_snake(camel_name):
    snake_name = ""  # create an empty list

    for char in camel_name: # iterate each character in inputted name
        if char.isupper():
            snake_name += "_"   # add an _ before the upper character

        snake_name += char.lower()     # add all the lowered case char from camel_name to snake_name 

    return snake_name


main()