# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

word_to_guess = "hello"
attemp_amount = 10
print("Welcome to the Hangman game!")
print(f"The word for today has {len(word_to_guess)} letter. Try to guess it! Good luck!")
display_word = ["_"] * len(word_to_guess)

while attemp_amount > 0:
    print("Word to guess:", " ".join(display_word))
    print(f"Attempt left {attemp_amount}")
    user_input = input("Please enter a single alphabet letter: ").lower()

    if not user_input.isalpha() or len(user_input) != 1:
        print("Input invalid!")
        continue
    elif user_input in word_to_guess:
        print("Correct guess!")
        for i, char in enumerate(word_to_guess):
            if char == user_input:
                display_word[i] = char
    else:
        print("Wrong guess!")
        attemp_amount -= 1

    if "_" not in display_word:
        print(f"Congratulation! You guessed the word: {word_to_guess}")
        break

if attemp_amount == 0:
    print(f"Sorry! The correct word is {word_to_guess}. Better luck next time!")
