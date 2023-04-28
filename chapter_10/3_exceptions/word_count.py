"""

    Title: Working with Multiple FIles
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "Let's add more books to analyze, but before we do, let's move 
    the bulk of this program to a function called count_words(). This will make 
    it easier to run the analysis for multiple books:"

"""

from pathlib import Path

# C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/3_exceptions/files/alice.txt 

def count_words(path):

    # Count the approximate number of words in a file.
    try:

        contents = path.read_text(encoding='utf-8')
    
    except FileNotFoundError:

        print(f"Sorry, the file {path} does not exist.")

    else: 

        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


#path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/3_exceptions/files/alice.txt')
#count_words(path)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:

    path = Path(f"C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/3_exceptions/files/{filename}")

    count_words(path)