# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

user_input = int(input("Please enter a number between 1 and 12: "))

if user_input < 1 or user_input > 12:
    print("Error")
else:
    if user_input == 1:
        print("January")
    elif user_input == 2:
        print("February")
    elif user_input == 3:
        print("March")
    elif user_input == 4:
        print("April")
    elif user_input == 5:
        print("May")
    elif user_input == 6:
        print("June")
    elif user_input == 7:
        print("July")
    elif user_input == 8:
        print("August")
    elif user_input == 9:
        print("September")
    elif user_input == 10:
        print("October")
    elif user_input == 11:
        print("November")
    else:
        print("December")