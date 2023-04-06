"""
    Title: Testing Multiple Conditions
    Author: Eric Matthes
    Date: 04/05/2023
    Description: "The if-elif-else chain is powerful but it's only 
    appropriate to use when you just need one test to pass.
    
    However, sometimes it's important to check all conditions of 
    an interest. In this case, you should use a series of simple 
    if statements with no elif or else blocks."

"""

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

    print("\nFinished making your pizza!")