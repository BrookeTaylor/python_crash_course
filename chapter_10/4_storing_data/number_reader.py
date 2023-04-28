"""

    Title: Using json.loads()
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Now we'll write a separate program that uses json.loads() to 
    read the list back into memory:"

"""

from pathlib import Path

import json

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/4_storing_data/files/numbers.json')

contents = path.read_text()

numbers = json.loads(contents)

print(numbers)