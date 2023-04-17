"""

    Title: Inheritance
    Author: Eric Matthes
    Date: 04/16/2023
    Description: "You don't always have to start from scratch when writing a 
    class. If the class you're writing is a specialized version of another 
    class you wrote, you can use inheritance. When one class inherits from 
    another, it takes on the attributes and methods of the first class. The 
    original class is called the parent class, and the new class is the child 
    class. The child class can inherit any or all of the attributes and methods 
    of its parent class, but it's also free to define new attributes and 
    methods of its own."

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



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

