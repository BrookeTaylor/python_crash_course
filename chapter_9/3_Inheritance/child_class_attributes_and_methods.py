"""

    Title: Defining Attributes and Methods for the Child Class
    Author: Eric Matthes
    Date: 04/16/2023
    Description: "once you have a child class that inherits from a parent 
    class, you can add any new attributes and methods necessary to 
    differentiate the child class from the parent class."

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

        # Print a statement showing the car's mileage.
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):

        # Set the odometer reading to the given value.
        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage

        else:

            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):

            # Add the given amount to the odometer reading.
            self.odometer_reading += miles



class ElectricCar(Car):
# Represent aspects of a car, specific to electric vehicles.

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    
    def describe_battery(self):

        # Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kWh battery.")



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


"""

    "We added a new attribute self.battery_size and set its initial value to 
    40. This attribute will be associated with all instances created from the 
    ElectricCar class but won't be associated with any instances of Car."

"""

