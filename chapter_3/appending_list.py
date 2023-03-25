"""
    Title: Adding Elements to a list
    Author: Eric Matthes
    Date: 03/24/2023
    Description: motorcycles list. 

    "Most lists you create will be dynamic, 
    meaning you'll build a list and then 
    add and remove elements from it as 
    your program runs its course."

"""

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')

print(motorcycles)


# Or you can append from an empty array.

# Building lists this way is very common, 
# because you often won't know the data your 
# users want to store in a program until after 
# the program is running.

bicycles = []

bicycles.append('trek')
bicycles.append('cannondale')
bicycles.append('redline')
bicycles.append('specialized')

print(bicycles)




# Inserting Elements into a List

loz = ['The Legend of Zelda (1986)', 'The Adventure of Link (1987)', 'A Link to the Past (1991)']

# print(loz)

loz.insert(0, 'Skyward Sword (2011)')
loz.insert(1, 'The Minish Cap (2004)')
loz.insert(2, 'Four Swords (2004)')
loz.insert(3, 'Ocarina of Time (1998)')

print(loz)

