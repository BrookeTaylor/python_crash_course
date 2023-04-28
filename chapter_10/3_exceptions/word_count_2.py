"""

    Title: Failing Silently
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "In the previous example, we informed our users that one of 
    the files was unavailable. But you don't need to report every exception you 
    catch. Sometimes, you'll want the program to fail silently when an 
    exception occurs and continue on as if nothing happened. To make a program 
    fail silently, you write a try block as usual, but you explicitly tell 
    Python to do nothing in the except block. Python has a pass statement that 
    tells it to do nothing in a block:"

"""

from pathlib import Path


def count_words(path):

    # Count the approximate number of words in a file.
    try:

        contents = path.read_text(encoding='utf-8')
    
    except FileNotFoundError:

        pass        # Python can pass on except. 

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