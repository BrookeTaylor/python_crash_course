"""

    Title: A List in a Dictionary continued...
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "When we loop through the dictionary, the value 
    associated with each person would be a list of languages rather 
    than a single language. Inside the dictionary's for loop, we use 
    another for loop to run through the list of languages associated 
    with each person:"

"""

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")