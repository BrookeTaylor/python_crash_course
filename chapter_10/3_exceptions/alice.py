"""

    Title: Handling the FileNotFoundError Exception
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "One common issue when working with files is handling missing 
    files. The file you're looking for might be in a different location, the 
    filename might be misspelled, or the file might not exist at all. You can 
    handle all of these situations with a try-except block.
    
    Let's try to read a file that doesn't exist. The following program tries to 
    read in the contents of Alice in Wonderland, but I haven't saved the file 
    alice.txt in the same directory as alice.py"

"""

from pathlib import Path

path = Path('alice.txt')


#contents = path.read_text(encoding='utf-8')
#FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

try: 

    contents = path.read_text(encoding='utf-8')

except FileNotFoundError:

    print(f"Sorry, the file {path} does not exist.")