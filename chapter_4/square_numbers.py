"""
    Title: Using the range() Function continued
    Author: Eric Matthes
    Date: 04/03/2023
    Description: "Python's range() function
    makes it easy to generate a series of numbers.

    You can create almost any set of numbers you 
    want to use the range() function. For example, 
    consider how you might make a list of the first 
    10 square numbers. In Python, two (**) represent 
    exponents."

"""

squares = []

for value in range(1, 11):

#### "To write this code more concisely, omit the 
#### temporary variable square and append each new value
#### directly to the list:"

#   square = value ** 2
#    squares.append(square)


#### "This line does the same work as the lines 
#### inside the for loop in the previous listing."
    squares.append(value**2)

print(squares)