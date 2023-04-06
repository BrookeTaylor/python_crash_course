"""
    Title: If Statements
    Author: Eric Matthes
    Date: 04/04/2023
    Description: "Programming often involves examining a set of conditions 
    and deciding which action to take based on those conditions. Python's 
    if statement allows you to examine the current state of a program and 
    respond appropriately to that state."  

"""

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())