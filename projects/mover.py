# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

from pathlib import Path

desktop = Path().home().joinpath("Desktop")
screenshots = desktop.joinpath("screenshots")
screenshots.mkdir(exist_ok=True)

for png_file in desktop.iterdir():
    if png_file.suffix == ".png":
        destination = screenshots.joinpath(png_file.name)
        png_file.replace(destination)
