# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path.cwd()

for level_1 in path.iterdir():
    if level_1.is_dir():
        for level_2 in level_1.iterdir():
            if level_2.is_file:
                if level_2.suffix == '.py':
                    print(f"{level_2.parent.name}/{level_2.name}")