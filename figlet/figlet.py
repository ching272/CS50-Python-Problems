from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
    f = sys.argv[2]
else:
    sys.exit("Invalid usage")

inp = input("Input: ").strip()
figlet.setFont(font = f)
print("Output: ")
print(figlet.renderText(inp))

