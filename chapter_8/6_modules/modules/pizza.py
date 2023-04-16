"""

    Title: pizza.py
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "pizza.py module for import"

"""
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")