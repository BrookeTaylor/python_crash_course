"""

    Title: Instance w/ cars
    Author: Eric Matthes
    Date: 04/16/2023
    Description: "Instance w/ cars."

"""
from modules.cars import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()