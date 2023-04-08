"""

    Title: Using a while Loop with Lists and Dictionaries
    Author: Eric Matthes
    Date: 04/08/2023
    Description: "We start with a list containing multiple instances 
    of 'cat'. After printing the list, Python enters the while loop 
    because it finds the value 'cat' in the list at least once. Once 
    inside the loop, Python removes the first instance of 'cat', 
    returns to the while line, and then reenters the loop when it 
    finds that 'cat' is still in the list. It removes each instance 
    of 'cat' until the value is no longer in the list, at which point 
    Python exits the loop and prints the list again:"

"""

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)