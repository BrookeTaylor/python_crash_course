"""

    Title: 
    Author: Eric Matthes
    Date: 04/28/2023
    Description: ""

"""

def get_formatted_name(first, last, middle=''):


# Generate a neatly formatted full name.
    if middle: 
        
        full_name = f"{first} {middle} {last}"
    
    else:

        full_name = f"{first} {last}"

    return full_name.title()

