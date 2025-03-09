# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

words = input("Please enter a string of words: ")
letter = input("Please enter a letter: ")

if letter in words:
    print(words.index(letter))
else:
    print("The letter is not in the string of words")