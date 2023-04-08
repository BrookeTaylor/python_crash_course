"""

    Title: Looping Through a Dictionary
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "You can access the value associated with any key 
    you care about inside the loop, by using the current key. Let's 
    print a message to a couple of friends about the languages they 
    choose. We'll loop through the names in the dictionary as we 
    did previously, but when the name matches one of our friends, 
    we'll display a message about their favorite language:"

"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends: 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")




print("\n")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("\n")




for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")