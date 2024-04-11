words = input("Greeting: ")

#split input into words
lowercase_words = words.lower()

#money check
if lowercase_words.startswith("h"):
    if lowercase_words.startswith("hello"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")    


    