# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

strings_input = input("Please enter three strings: ")
words = (strings_input.split())
first_word = words[0]
second_word = words[1]
third_word = words[2]

if len(first_word) > len(second_word) and len(first_word) > len(third_word):
    print(f"{len(first_word), {first_word}}")
elif len(second_word) > len(first_word) and len(second_word) > len(third_word):
    print(f"{len(second_word), {second_word}}")
else:
    print(f"{len(third_word)}, {third_word}")