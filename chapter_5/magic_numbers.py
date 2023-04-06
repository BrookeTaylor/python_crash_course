"""
    Title: Numerical Comparisons
    Author: Eric Matthes
    Date: 04/04/2023
    Description: "Testing numerical values is pretty straightforward."  

"""

# "You can also test to see if two numbers are not equal."

i = 18 

if i == 18: 
    print("i equals 18, correct!")

if i != 9:
    print("i isn't 9, that's incorrect.\n")


# "You can include various mathematical comparisons in your conditional 
# statements as well, such as less than, less than or equal to, greater than, 
# and greater than or equal to:"

age = 21

if age < 23:
    print("age is less than 23.")

if age <= 23:
    print("age is less than or equal to 23.")

if age > 23:
    print("age is greater than 23")                     # Returns false. 

if age >= 23: 
    print("age is greater than or equal to 23.")        # Returns false. 

"""

    Title: Checking Multiple Conditions
    Author: Eric Matthes
    Date: 04/05/2023
    Description: "You may want to check multiple conditions at the 
    same time. For example, sometimes you might need two conditions 
    to be True to take an action."  

"""

if i < age and age > i:
    print("i is less than age; and age is greater than i.")