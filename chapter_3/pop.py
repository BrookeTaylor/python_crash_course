"""
    Title: Deleting Items and Popping.
    Author: Eric Matthes
    Date: 03/24/2023
    Description: delete vs pop. 

    "Sometimes you'll want to use 
    the value of an item after you 
    remove it from a list. In a web 
    application, you might want 
    to remove a user from a list of 
    active members and then add that 
    user to a list of inactive 
    members.

    The pop() method removes the last 
    item in a list, but it lets you 
    work with that item after removing
    it. The term pop comes from thinking 
    of a list as a stack of items and 
    popping one item off the top of 
    the stack."

"""
motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)

print(f'The last motorcycle my father owned was a {popped_motorcycle.title()}.')