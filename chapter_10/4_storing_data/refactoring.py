"""

    Title: Refactoring
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Often, you'll come to a point where your code will work, but 
    you'll recognize that you could improve the code by breaking it up into a 
    series of functions that have specific jobs. This process is called 
    refactoring. Refactoring makes your code cleaner, easier to understand, 
    and easier to extend.
    
    We can refactor remember_me.py by moving the bulk of its logic into one or 
    more functions. The focus of remember_me.py is on greeting the user, so 
    let's move all of our existing code into a function called greet_user():"

"""

from pathlib import Path
import json

def greet_user():

    # Greet the user by name.
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

greet_user()

