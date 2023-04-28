"""

    Title: Writing Multiple Lines
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "The write_text() method does a few things behind the scenes. 
    If the file that path points to doesn't exist, it creates that file. Also, 
    after writing the string to the file, it makes sure the file is closed 
    properly. Files that aren't closed properly can lead to missing or 
    corrupted data."

"""

from pathlib import Path

contents = "I love Programming in Python!\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/2_writing_to_a_file/files/programming_2.txt')

path.write_text(contents)