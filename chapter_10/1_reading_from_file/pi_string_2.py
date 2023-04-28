"""

    Title: Working with a File's Contents Continued.
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "The variable pi_string contains the whitespace that was on 
    the left side of the digits in each line, but we can get rid of that by 
    using lstrip() on each line:"

"""

from pathlib import Path

path = Path("C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/1_reading_from_file/files/pi_digits.txt")

contents = path.read_text()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    
    pi_string += line.lstrip()

print(pi_string)

print(len(pi_string))