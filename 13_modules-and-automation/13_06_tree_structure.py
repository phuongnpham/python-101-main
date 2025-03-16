# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path.cwd()

for python_file in path.rglob("*.py"):
    print(f"{python_file.parent.name}/{python_file.name}")