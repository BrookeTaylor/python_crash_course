"""

    Title: Looping Through a Dictionary
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "If you are primarily interested in the values that 
    a dictionary contains, you can use the values() method to return 
    a sequence of values without any keys."

"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())