"""

    Title: Using get() to Access Values
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "Using keys in square brackets to retrieve the 
    value you're interested in from a dictionary might cause one 
    potential problem: if the key you ask for doesn't exist, 
    you'll get an error."

"""

alien_0 = {'color': 'green', 'speed': 'slow'}

# "Let's see what happens when you ask for the point value of an 
# alien that doesn't have a point value set:"

# print(alien_0['points'])        #KeyError: 'points'



"""

    "For dictionaries specifically, you can use the get() method to 
    set a default value that will be returned if the requested key 
    doesn't exist.

    The get() method requires a key as a first argument. As a second 
    optional argument, you can pass the value to be returned if the 
    key doesn't exist:"

"""
point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)