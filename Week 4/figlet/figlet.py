from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    text_input = input("Input: ")
    print(figlet.renderText(text_input))
elif len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid Usage")
    else:
        figlet.setFont(font=sys.argv[2])
        text_input = input("Input: ")
        print(figlet.renderText(text_input))
else:
    sys.exit("Invalid Usage")
