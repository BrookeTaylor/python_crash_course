"""

    Title: A List in a Dictionary
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "Rather than putting a dictionary inside a list, 
    it's sometimes useful to put a list inside a dictionary."

"""

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize that order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")