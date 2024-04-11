vowels = ["a", "e", "i", "o", "u"]
user_input = input("Input: ")
output = ""
for char in user_input:
    if char not in vowels:
        output += char
print("Output:", output)