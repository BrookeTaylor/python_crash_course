"""
    Title: Using Multiple Lists
    Author: Eric Matthes
    Date: 04/06/2023
    Description: "A dictionary in Python is a collection of key-value 
    pairs. Each key is connected to a value, and you can use a key 
    to access the value associated with that key. A key's value can 
    be a number, a string, a list, or even another dictionary. In 
    fact, you can use any object that you can create in Python as
    as a value in a dictionary. 
    
    In Python, a dictionary is wrapped in braces ({}) with a series 
    of key-value pairs inside the braces."

"""

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")