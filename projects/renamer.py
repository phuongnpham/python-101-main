# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

from pathlib import Path

desktop = Path().home().joinpath("Desktop")
screenshots = desktop.joinpath("screenshots")
screenshots.mkdir(exist_ok=True)
counter = 0

for png_file in desktop.iterdir():
    if png_file.suffix == ".png":
        counter += 1
        png_file_rename = f"screenshot_{counter}.png"
        destination = screenshots.joinpath(png_file_rename)
        png_file.rename(destination)