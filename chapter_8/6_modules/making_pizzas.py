"""

    Title: Importing an Entire Module
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "This file imports the module we just created and 
    then makes two calls to make_pizza():"

"""

# "When Python reads this file, the line import pizza tells Python to 
# open the file pizza.py and copy all the functions from it into 
# this program."
from modules import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

