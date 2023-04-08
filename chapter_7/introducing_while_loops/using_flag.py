"""

    Title: Using a Flag 
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "In the previous example, we had the program perform 
    certain tasks while a given condition was true. But what about 
    more complicated programs in which many different events could 
    cause the program to stop running?
    
    For a program that should run only as long as many conditions 
    are true, you can define one variable that determines whether or 
    not the entire program is active. This variable, called a flag, 
    acts as a signal to the program. We can write our programs so 
    they run while the flag is set to True and stop running when any 
    of several events sets the value of the flag to False."

"""

prompt = "\tTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active: 
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)