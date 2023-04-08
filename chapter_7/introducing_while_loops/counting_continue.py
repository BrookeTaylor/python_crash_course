"""

    Title: Using continue in a Loop
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "Rather than breaking out of a loop entirely without 
    executing the rest of its code, you can use the continue 
    statement to return to the beginning of the loop, based on the 
    result of a conditional test."

"""

current_number = 0
while current_number < 10:
    current_number += 1 
    if current_number % 2 == 0:
        continue 
print(current_number)
