"""

    Title: Positional Arguments 
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "When you call a function, Python must match each 
    argument in the function call with a parameter in the function 
    definition. The simplest way to do this is based on the order of 
    the arguments provided. Values matched up this way are called 
    positional arguments."

"""
def describe_pet(animal_type, pet_name):

    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('boxer dog', 'Ollie')

# Multiple Function Calls 
# You can call a function as many times as needed.
describe_pet('husky dog', 'Luna')