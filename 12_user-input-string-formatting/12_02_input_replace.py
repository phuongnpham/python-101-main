# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

words = input("Please enter a string of words: ")
symbol = input("Please enter a symbol: ")

words_lowercase = words.lower()
char = words_lowercase[0]

while char:
    new_words = words_lowercase.replace(char, symbol)
    print(new_words)
    break