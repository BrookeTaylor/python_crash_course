"""
    Title: Using the range() Function continued
    Author: Eric Matthes
    Date: 04/03/2023
    Description: "Python's range() function
    makes it easy to generate a series of numbers.

    We can also use the range() function to 
    tell Python to skip numbers in a given range. 
    If you pass a third argument to range(), 
    Python uses that value as a step size when 
    generating numbers."

"""

even_numbers = list(range(2, 11, 2))

print(even_numbers)