"""

    Title: Using -as- to Give a Function an Alias
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "If the name of a function you're importing might 
    conflict with an existing name in your program, or if the function 
    name is long, you can use a short, unique alias-an alternative 
    name similar to a nickname for the function. You'll give the 
    function this special nickname when you import the function.
    
    Here we give the function make_pizza() an alias, mp(), by 
    importing make_pizza as mp. The keyword renames a function using 
    the alias you provide:"

"""

# "You can also import a specific function from a module."
from modules.pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

"""

    "The import statement shown here renames the function make_pizza() 
    to mp() in this program. Anytime we want to call make_pizza() we 
    can simply write mp() instead, and Python will run the code in 
    make_pizza() while avoiding any confusion with another 
    make_pizza() function you might have written in this program 
    file."

"""