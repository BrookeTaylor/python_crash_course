"""
    Title: Removing Key-Value Pairs
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "When you no longer need a piece of information 
    that's stored in a dictionary, you can use the del statement to 
    completely remove a key-value pair."

"""

alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

del alien_0['points']

print(alien_0)
