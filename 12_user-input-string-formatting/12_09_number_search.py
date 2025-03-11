# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user_input = int(input("Please enter a number between 0 and 1,000,000,000: "))

number = 0
print("Finding the number")
while True:
    if number == user_input:
        print(number)
        break
    number += 1