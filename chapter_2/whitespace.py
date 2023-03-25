"""
    Title: Working with Whitespace
    Author: Eric Matthes
    Date: 03/23/2023
    Description: Working with whitespace.

"""

# To add a tab to your text, use the 
# character combination \t:
# print("\tPython")


# To add a newline in a string, use the 
# character combination \n:
# print("Languages: \n\tJavaScript\n\tPython")

favorite_language = "python "
Favorite_language = "javaScript"

# print(f"{favorite_language.title()}and {Favorite_language.title()}")

print(f"{favorite_language.rstrip().title()} and {Favorite_language.title()}!")