"""

    Title: Checking Multiple Conditions
    Author: Eric Matthes
    Date: 04/05/2023
    Description: "Sometimes it's important to check whether a list contains a 
    certain value before taking an action. For example, you might want to check 
    whether a new user name already exists in a list of current usernames 
    before completing someone's registration on a website.
    
    To find out whether a particular value is already in a list, use the 
    keyword in."  

"""

cars = ['audi', 'bmw', 'subaru', 'toyota']

if "audi" in cars: 
    print(f"{cars[0].title()} is in the variable, 'cars'.")

if "chevy" not in cars: 
    print("Chevy is not in the variable, 'cars'.")