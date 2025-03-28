# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

from pathlib import Path

path = Path.cwd()
any_extension = []

for level_1 in path.iterdir():
    if level_1.is_dir():
        for level_2 in level_1.iterdir():
            if level_2.suffix == '.jpg':
                print(f"{level_2.resolve()}")
            elif level_2.is_file:
                any_extension.append(level_2.suffix)
    else:
        if level_1.suffix == '.jpg':
            print(f"{level_1.resolve()}")
        elif level_1.is_file:
            any_extension.append(level_1.suffix)
print(f"List of other types of extension were found: {list(set(any_extension))}")