"""
    Title: Sorting a List Temporarily
            with the sorted() Method.
    Author: Eric Matthes
    Date: 03/24/2023
    Description: 

    "To maintain the original order of a list 
    but present it in a sorted order, you can 
    use the sorted() function. The sorted() 
    function lets you display your list in a 
    particular order, but doesn't affect the 
    actual order of the list."

"""
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)