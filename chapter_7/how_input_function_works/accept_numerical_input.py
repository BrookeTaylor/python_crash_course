"""

    Title: Using int() to Accept Numerical Input
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "When you use the input() function, Python 
    interprets everything the user enters as a string.
    
    We can resolve this issue by using the int() function, which 
    converts the input string into a numerical value."

"""

age = input("how old are you? ")

age = int(age)

if age >= 18:
    print("You're 18 or older!")

else:
    print("Still some growing up to do.")