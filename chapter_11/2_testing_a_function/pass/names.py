"""

    Title: Testing a Function continued.
    Author: Eric Matthes
    Date: 04/24/2023
    Description: ""

"""

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:

    first = input("\nPlease give me a first name: ")

    if first == 'q':

        break

    last = input("Please give me a last name: ")

    if last == 'q':

        break


formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted named: {formatted_name}.")

