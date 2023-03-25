"""
    Title: Removing an Item by Value.
    Author: Eric Matthes
    Date: 03/24/2023
    Description: 

    "Sometimes you won't know the position 
    of the value you want to remove from 
    a list. if you only know the value of 
    the item you want to remove, you can use 
    the remove() method."

"""

motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']

motorcycles.remove('ducati')

print(motorcycles)


# "You can also use the remove() method to work with 
# a value that's being removed from a list."

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

too_much = 'specialized'
bicycles.remove(too_much)

print(bicycles)
print(f"\nThe {too_much} bicycle was too much for me.")