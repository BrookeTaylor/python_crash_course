"""

    Title: Making an Instance from a Class
    Author: Eric Matthes
    Date: 04/16/2023
    Description: "Think of a class as a set of instructions for how to make an 
    instance. The Dog class is a set of instructions that tells Python how to 
    make individual instances representing specific dogs."

"""
from modules.dog import Dog

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

"""

    Accessing Attributes

    "To access the attributes of an instance, you use dot notation. We access 
    the value of my_dog's attribute name by writing:"

        my_dog.name

    
    Calling Methods

        "After we create an instance from the class Dog, we can use dot 
        notation to call any method defined in Dog. Let's make our dog sit and 
        roll over:"

"""
my_dog.sit()
my_dog.roll_over()


"""

    Creating Multiple Instances

    "You can create as many instances from a class as you need. Let's create a 
    second dog called your_dog:"

"""
your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()


"""

    "Even if we used the same name and age for the second dog, Python would 
    still create a separate instance from the Dog class. You can make as many 
    instances from one class as you need, as long as you give each instance a 
    unique variable name or it occupies a unique spot in a list or dictionary."

"""
 
