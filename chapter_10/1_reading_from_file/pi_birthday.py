"""

    Title: Large Files: One Million Digits.
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "I've always been curious to know if my birthday appears 
    anywhere in the digits of pi. Let's use the program we just wrote to find 
    out if someone's birthday appears anywhere in the first million digits of 
    pi. We can do this by expressing each birthday as a string of digits and 
    seeing if that string appears anywhere in pi_string:"

"""

from pathlib import Path

path = Path("C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/1_reading_from_file/files/pi_million_digits.txt")

contents = path.read_text()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    
    pi_string += line.lstrip()



birthday = input("Enter your birthday, in the from mmddyy: ")

if birthday in pi_string:

    print("Your birthday appears in the first million digits of pi!")

else:

    print("Your birthday does not appear in the first million digits of pi.")
