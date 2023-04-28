"""

    Title: Reading User-Generated Data
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Now let's write a new program that greets a user whose name 
    has already been stored:"

"""

from pathlib import Path
import json

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/4_storing_data/files/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")

