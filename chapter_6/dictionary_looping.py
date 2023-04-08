"""

    Title: Looping Through a Dictionary
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "A single Python dictionary can contain jsut a few 
    key-value pairs or millions of pairs. Because a dictionary can 
    contain large amounts of data, Python lets you loop through a 
    dictionary."

"""

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}


for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


print("\n")
"""

    "This code tells Python to loop through each key-value pair in 
    the dictionary. As it works through each pair the key is assigned 
    to name, and the value is assigned to the variable language."

"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")



print("\n")
"""

    "Looping Through All the Keys in a Dictionary: 

    The keys() method is useful when you don't need to work with all 
    of the values in a dictionary."

"""

for name in favorite_languages.keys():
    print(name.title())


"""

    "Looping through the keys is actually the default behavior when 
    looping through a dictionary, so this code would have exactly the 
    same output if you wrote:"

for name in favorite_languages: 

"""
