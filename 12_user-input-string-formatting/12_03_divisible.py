# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

num_input = int(input("Please enter a number between 1 and 1,000,000,000: "))
if num_input % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")