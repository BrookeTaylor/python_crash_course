"""
    Title: Slicing a list.
    Author: Eric Matthes
    Date: 04/03/2023
    Description: "To make a slice, you specify 
    the index of the first and last elements 
    you want to work with. As with the 
    range() function, Python stops one item 
    before the second index you specify."

"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])     #['charles', 'martina', 'michael']
print(players[2:4])     #['michael', 'florence']


# "If you omit the first index in a slice, Python
# automatically starts your slice at the 
# beginning of the list."

print(players[:2])      #['charles', 'martina']


# "A similar syntax works if you want a slice that includes 
# the end of a list."

print(players[3:])      #['florence', 'eli']


# "This syntax allows you to output all of the elements 
# from any point in your list to the end, regardless of 
# the length of the list."

print(players[-3:])     #['michael', 'florence', 'eli']