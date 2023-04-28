"""

    Title: Refactoring continued
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Because we're using a function now, we rewrite the comments 
    as a docstring that reflects how the program currently works. This file is 
    a little cleaner, but the function greet_user() is doing more than just 
    greeting the user--it's also retrieving a stored username if one exists and 
    prompting for a new username if one doesn't. 
    
    Let's refactor greet_user() so it's not doing so many different tasks. 
    We'll start by moving the code for retrieving a stored username to a 
    separate function:"

"""

from pathlib import Path
import json



def get_stored_username(path):

    # Get stored username if available.
    if path.exists():

        contents = path.read_text()
        username = json.loads(contents)
        return username
    
    else:

        return None



def greet_user():

    # Greet the user by name.
    path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/4_storing_data/files/username.json')

    username = get_stored_username(path)

    if username:

        print(f"Welcome back, {username}!")

    else:

        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

