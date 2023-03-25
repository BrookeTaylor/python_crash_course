"""
    Title: Popping position.
    Author: Eric Matthes
    Date: 03/24/2023
    Description: 

    "You can use pop() to remove 
    an item from any position in a list 
    by including the index of the item 
    you want to remove in parentheses."

"""

# According to The Legend of Zelda Timeline, 
# in the Fallen Hero's Timeline - the third 
# game released, would appear last on our list here. 
loz = ['The Legend of Zelda (1986)', 'The Adventure of Link (1987)', 'A Link to the Past (1991)']


loz.insert(0, 'Skyward Sword (2011)')
loz.insert(1, 'The Minish Cap (2004)')
loz.insert(2, 'Four Swords (2004)')
loz.insert(3, 'Ocarina of Time (1998)')

# Popped out the third installment of the series.
popped_loz = loz.pop(5)

print(f"To play in chronological order: {loz[0]}, {loz[1]}, {loz[2]}, {loz[3]}, {loz[4]}, {loz[5]}, and finally {popped_loz}")