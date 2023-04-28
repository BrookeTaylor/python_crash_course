"""

    Title: Using json.dumps()
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Let's write a short program that stores a set of numbers and 
    another program that reads these numbers back into memory. The first 
    program will use json.dumps() to store the set of numbers, and the second 
    program will use json.loads().
    
    The json.dumps() function takes one argument: a piece of data that should 
    be converted to the JSON format. The function returns a string, which we 
    can then write to a data file:"

"""

from pathlib import Path

# "We first import the json module, and then create a list of numbers to 
# work with."
import json


numbers = [2, 3, 5, 7, 11, 13]

# "Then we choose a filename in which to store the list of numbers. It's 
# customary to use the file extension .json to indicate that the data in the 
# file is stored in the JSON format."
path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/4_storing_data/files/numbers.json')


# "Next, we use the json.dumps() function to generate a string containing the 
# JSON representation of the data we're working with."
contents = json.dumps(numbers)


# "Once we have this string (above), we write it to the file using the same 
# write_text() method we used earlier."
path.write_text(contents)

