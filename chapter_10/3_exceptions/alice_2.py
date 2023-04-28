"""

    Title: Analyzing Text
    Author: Eric Matthes
    Date: 04/23/2023
    Description: "You can analyze text files containing entire books. Many 
    classic works of literature are available as simple text files because 
    they are in the public domain. The texts used in this section come from 
    Project Gutenberg (https://gutenberg.org). Project Gutenberg maintains a 
    collection of literary works that are available in the public domain, and 
    it's a great resource if you're interested in working with literary texts 
    in your programming projects.
    
    Let's pull in the text of Alice in Wonderland and try to count the number 
    of words in the text. To do this, we'll use the string method split(), 
    which by default splits a string wherever it finds any whitespace:"

"""

from pathlib import Path

path = Path('C:/Users/Brooke/Documents/buwebdev/python_crash_course/chapter_10/3_exceptions/files/alice.txt')

try:

    contents = path.read_text(encoding='utf-8')

except FileNotFoundError:

    print(f"Sorry, the file {path} does not exist.")

else:

    # Count the approximate number of words in the file:
    words = contents.split()

    num_words = len(words)
    
    print(f"The file {path} has about {num_words} words.")