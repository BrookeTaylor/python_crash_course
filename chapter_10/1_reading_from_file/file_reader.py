"""

    Title: Reading from a File
    Author: Eric Matthes
    Date: 04/17/2023
    Description: "When you want to work with the information in a text file, 
    the first step is to read the file into memory. You can then work through 
    all of the file's contents at once or work through the contents 
    line by line.

    Here's a program that opens this file, reads it, and prints the contents 
    of the file to the screen:"

"""

from pathlib import Path

path = Path("C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/1_reading_from_file/files/pi_digits.txt")

contents = path.read_text()

print("\nPi to thirty digits, three rows of ten.\n")
print(contents)


