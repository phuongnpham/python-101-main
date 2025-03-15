# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

number_to_guess = random.randint(1, 1000)
attemp_amount = 10
user_input = None

while attemp_amount > 0:
    print(f"Attempt left: {attemp_amount}")
    user_input = int(input("Please enter a number between 1 and 1000: "))
    if user_input == number_to_guess:
        print(f"Congratulation! You guessed it right")
        break
    else:
        if user_input > number_to_guess:
            print(f"Your number {user_input} is bigger than our number")
        else:
            print(f"Your number {user_input} is smaller than our number")
        attemp_amount -= 1

if attemp_amount == 0:
    print(f"Sorry, you did not guess {number_to_guess} correctly. Better luck next time!")