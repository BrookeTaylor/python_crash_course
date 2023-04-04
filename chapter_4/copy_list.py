"""
    Title: Copying a List
    Author: Eric Matthes
    Date: 04/03/2023
    Description: "Often, you'll want to start 
    with an existing list and make an entirely 
    new list based on the first one."

"""

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]


# "To prove that we actually have two separate lists, 
# we'll add a new food to each list and show that 
# each list keeps track of the appropriate 
# person's favorite foods:"
my_foods.append('cannoli')
friend_foods.append('ice cream')



print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)