"""

    Title: Handling the ZeroDivisionError Exception
    Author: Eric Matthes
    Date: 04/22/2023
    Description: "Let's look at a simple error that causes Python to raise an 
    exception. You probably know that it's impossible to divide a number by 
    zero, but let's ask Python to do it anyway:"

"""


#print(5/0)
#ZeroDivisionError: division by zero

try:
    print(5/0)

except ZeroDivisionError:
    print("You can't divide by zero!")