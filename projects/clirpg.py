# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

name = input("What's your name? ")
print(f"Welcome {name} to our CLI RPG world!")
print("You're in an empty room and have a choice between 2 doors: left door or right door")
print("""What's your choice?
      1. Left door
      2. Right door""")
first_choice = input(" ")
while first_choice:
    if first_choice == "1":
        print("You're in an another empty room")
        break
    elif first_choice == "2":
        print("Oh no! You encounter a dragon!")
        break
    else:
        input("Please enter 1 for left door or 2 for right door: ")
print("Do you want to return to the previous room or explore further?")
print("""What's your choice?
      1. Return to previous room and end the game
      2. Explore further""")
second_choice = input("What is your choice: 1 or 2? ")
while second_choice:
    if second_choice == "1":
        print("You're return to previous room and end the game")
        break
    elif second_choice == "2":
        print("Ok! Exploring further")
        if first_choice == "1":
            print("""You see a sword. Do you want to
      1. Take it
      2. Leave it""")
            third_choice = input("What is your choice: 1 or 2? ")
            print("You're now back to previous room and open the right door")
            if third_choice == "1":
                print("You're the winner! You defeat the dragon!")
                break
            elif third_choice == "2":
                print("Oh no! You're eaten by the dragon.")
                break
            else:
                print("Please enter 1 or 2")
        elif first_choice == "2":
            print("Oh no! You're eaten by the dragon.")
            break
        else:
            input("Please enter 1 or 2: ")
    else:
        input("Please enter a correct choice: 1 or 2: ")