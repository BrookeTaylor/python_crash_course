"""
    Title: Python Lists
    Author: Eric Matthes
    Date: 03/24/2023
    Description: Bicycles list. 

    "It's a good idea to make the 
    name of your list plural, such as 
    letters, digits, or names. 

"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

message = f"My first bicycle was a {bicycles[0].title()}."




print(bicycles)  
print(bicycles[0]) # works just like in JavaScript! Arrays start counting at 0, 1, 2, etc
print(bicycles[-1].upper())
print(message)