"""
    Title: Using if Statements with Lists
    Author: Eric Matthes
    Date: 04/05/2023
    Description: "You can do some interesting work when you combine 
    lists and if statements. You can watch for special values that 
    need to be treated differently than other values in the list. 
    You can efficiently manage changing conditions, such as the 
    availability of certain items in a restaurant throughout a 
    shift."

"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings: 

    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")