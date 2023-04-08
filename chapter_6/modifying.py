"""
    Title: Modifying Values in a Dictionary
    Author: Eric Matthes
    Date: 04/06/2023
    Description: "To modify a value in a dictionary, give the name of 
    the dictionary with the key in square brackets and then the new 
    value you want associated with that key."

"""

alien_0 = {'color': 'green'}

print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'

print(f"The alien is now {alien_0['color']}")



"""
    Title: Modifying Values in a Dictionary
    Author: Eric Matthes
    Date: 04/06/2023
    Description: "...let's track the position of an alien that can 
    move at different speeds. We'll store a value representing the 
    alien's current speed and then use it to determine how far to 
    the alien should move:"

"""

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right. 
# Determine how far to move the alien based on its current speed. 

if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: 
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment. 
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")