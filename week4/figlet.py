import sys

import random

#from the specifications
from pyfiglet import Figlet

figlet = Figlet()

#for no additional command line arguments
if len(sys.argv) == 1:
    isRandomFont = True
#in case two arguments are provided specifying the font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False # do not give me a random font because I have it specified.
else:
    print("invalid")
    sys.exit(1)

figlet.getFonts()

message = input("Input: ")
#ask for user input for the string on which he/she would like the font to be applied

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2]) #in case the font was provided, choose the font from the figlet module
    except:
        print("invalid")
        sys.exit(1)
else:

    font = random.choice(figlet.getFonts()) # in case the font was not provided, get a random font from the figlet module
    figlet.setFont(font = font)
#message = input("input: ")

print("Output: ")
print(figlet.renderText(message))

#   f = random.choice(figlet.getFonts())
#    figlet.setFont(font = f)