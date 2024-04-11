import string 

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():     # check if the first 2 chars are digits
            for i in range(1, len(s) - 1):        # iterates over string s excluding the first and last character
                if s[i].isdigit() and s[i + 1].isalpha():        #if there is a number before a letter
                    return False
                elif s[i].isdigit() and s[i] == "0":   #check to see if digit starts with 0 -> NEED FIXING 
                    return False
                elif has_punctuation(s):
                    return False

            return True


def has_punctuation(s):
    for char in s:
        if char in string.punctuation:
            return True
    return False


def zero_start(s):
    pass

main()




