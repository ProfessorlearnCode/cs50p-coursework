import sys
import random
import pyfiglet

figlet = pyfiglet.Figlet()

if len(sys.argv) == 1:
    print("No arguments given")
    random_font = random.choice(figlet.getFonts())
    user_input = input("Input: ")
    print(pyfiglet.figlet_format(user_input, font = random_font))
    print(random.choice(figlet.getFonts()))

elif len(sys.argv) > 1:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font" or sys.argv[1] == "renders") and (sys.argv[2] in figlet.getFonts()):
        user_font = sys.argv[2]
        user_input = input("Input: ")
        print(pyfiglet.figlet_format(user_input, font = user_font))
c
    else:
        sys.exit("invalid Usage1")

else:
    sys.exit("Invalid Usage2")