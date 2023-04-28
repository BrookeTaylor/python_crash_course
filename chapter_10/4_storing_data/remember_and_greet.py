"""

    Title: Saving and Reading User-Generated Data
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "We need to combine these two programs into one file. When 
    someone runs this program, we want to retrieve their username from memory 
    if possible; if not, we'll prompt for a username and store it in 
    username.json for next time. We could write a try-except block here to 
    respond appropriately if username.json doesn't exist, but instead we'll use 
    a handy method from the pathlib module:"

"""

from pathlib import Path
import json

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/4_storing_data/files/username.json')

if path.exists():

    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")

else: 

    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")