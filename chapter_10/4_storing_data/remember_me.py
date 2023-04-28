"""

    Title: Saving User-Generated Data
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Saving data with json is useful when you're working with 
    user-generated data, because if you don't store your user's information 
    somehow, you'll lose it when the program stops running. Let's look at an 
    example where we prompt the user for their name the first time they run a 
    program and then remember their name when they run the program again."

"""

from pathlib import Path
import json

username = input("What is your name? ")

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/4_storing_data/files/username.json')

contents = json.dumps(username)

path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")