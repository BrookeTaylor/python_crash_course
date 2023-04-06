"""
    Title: The if-elif-else
    Author: Eric Matthes
    Date: 04/05/2023
    Description: "Often, you'll need to test more than two possible 
    situations, and to evaluate these you can use Python's 
    if-elif-else syntax. Python executes only one block in an 
    if-elif-else chain. It runs each conditional test in order, until 
    one passes. When a test passes, the code following that test is 
    executed and Python skips the rest of the tests."

"""

age = 12

# if age < 4: 
#     print("Your admission cost is $0.")

# elif age < 18: 
#     print("Your admission cost is $25.")

# else:
#     print("Your admission cost is $40.")


if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65: 
    price = 40


# "Omitting the else Block
# Python does not require an else block at the end of an 
# if-elif chain."

elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")