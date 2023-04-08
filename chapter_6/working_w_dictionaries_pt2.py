"""
    Title: A Dictionary of similar Objects
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "You can also use a dictionary to store one kind of 
    information about many objects."

"""

favorite_languages = {

    'jen': 'python',
# "As you can see, we've broken a larger dictionary into several 
# lines. 
    'sarah': 'c',
# "When you know you'll need more than one line to define 
# a dictionary, press ENTER after the opening brace."
    'edward': 'rust',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}.")