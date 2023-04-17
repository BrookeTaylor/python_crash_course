"""

    Title: Working with Classes and Instances
    Author: Eric Matthes
    Date: 04/16/2023
    Description: "You can use classes to represent many real-world situations. 
    Once you write a class, you'll spend most of your time working with 
    instances created from that class. One of the first tasks you'll want to do 
    is modify the attributes associated with a particular instance. You can 
    modify the attributes of an instance directly or write methods that update 
    attributes in specific ways."

"""
class Car:

    # A simple attempt to represent a car. 
    def __init__(self, make, model, year):

        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0 
    
    def get_descriptive_name(self):

        # Return a neatly formatted descriptive name.
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):

        # Print a statement showing the car's milage.
        print(f"This car has {self.odometer_reading} miles on it.")

