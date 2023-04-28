"""

    Title: Large Files: One Million Digits.
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "So far, we've focused on analyzing a text file that contains 
    only three lines, but the code in these examples would work just as well on 
    much  larger files. If we start with a text file that contains pi to 
    1,000,000 decimal places, instead of just 30, we can create a single string 
    containing all these digits. We don't need to change our program at all, 
    except to pass it a different file. We'll also print just the first 50 
    decimal places, so we don't have to watch a million digits scroll by in 
    the terminal:"

"""

from pathlib import Path

path = Path("C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/1_reading_from_file/files/pi_million_digits.txt")

contents = path.read_text()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")

print(len(pi_string))