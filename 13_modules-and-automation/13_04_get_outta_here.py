# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys

while True:
    user_input = input("Please enter something:> ")

    if user_input.lower() == "quit":
        print("Exit the loop")
        sys.exit()

        