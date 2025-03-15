# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime

current_date_time = datetime.now()
format_current_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time {format_current_date_time}")