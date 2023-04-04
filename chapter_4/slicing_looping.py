"""
    Title: Looping Through a Slice
    Author: Eric Matthes
    Date: 04/03/2023
    Description: "You can use a slice in 
    a for loop if you want to loop through 
    a subset of the elements in a list."

"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())