"""

    Title: Working with a File's Contents
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "After you've read the contents of a file into memory, you can
    do whatever you want with that data, so let's briefly explore the digits of 
    pi. First, we'll attempt to build a single string containing all the digits 
    in the file with no whitespace in it:"

"""

from pathlib import Path

path = Path("C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/1_reading_from_file/files/pi_digits.txt")

contents = path.read_text()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    
    pi_string += line

print(pi_string)

print(len(pi_string))