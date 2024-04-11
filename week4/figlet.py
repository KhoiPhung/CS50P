import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 1:
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print(figlet.renderText(user_input))
            




