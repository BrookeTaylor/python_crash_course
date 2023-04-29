"""

    Title: A Failing Test
    Author: Eric Matthes
    Date: 04/28/2023
    Description: "Let's modify get_formatted_name() so it can handle middle 
    names, but let's do so in a way that breaks the function for names with 
    just a first and last name, like Janis Joplin.
    
    Here's a new version of get_formatted_name() that requires a middle name 
    argument:"

"""

def get_formatted_name(first, middle, last):

    # Generate a neatly formatted full name.
    full_name = f"{first} {middle} {last}"
    return full_name.title()

