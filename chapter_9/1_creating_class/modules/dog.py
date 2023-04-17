"""

    Title: Creating and Using a Class
    Author: Eric Matthes
    Date: 04/16/2023
    Description: The __init__() Method

    "A function that's part of a class is a method. Everything you learned 
    about functions applies to methods as well; the only practical difference 
    for now is the way we'll call methods. The __init__() method is a special 
    method that Python runs automatically whenever we create a new instance 
    based on the Dog class. This method as two leading underscores and two 
    trailing underscores, a convention that helps prevent Pythons default 
    method names from conflicting with your method names. Make sure to use two 
    underscores on each side of __init__(). If you use just one on each side, 
    the method won't be called automatically when you use your class, which can 
    result in errors that are difficult to identify."

"""

class Dog:

    def __init__(self, name, age):

        # Initialize name and age attributes.
        self.name = name
        self.age = age

    def sit(self):

        # Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):

        #simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")

