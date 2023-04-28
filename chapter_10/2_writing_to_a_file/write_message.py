"""

    Title: Writing to a File
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "One of the simplest ways to save data is to write it to a 
    file. When you write text to a file, the output will still be available 
    after you close the terminal containing your program's output. You can 
    examine output after a program finishes running, and you can share the 
    output files with others as well. You can also write programs that read the 
    text back into memory and work with it again later."

"""

from pathlib import Path

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/2_writing_to_a_file/files/programming.txt')

path.write_text('I love programming in Python!')


# "Python can only write strings to a text file. If you want to store numerical 
# data in a text file, you'll have to convert the data to string format first 
# using the str() function."
