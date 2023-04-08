"""

    Title: Letting the User Choose When to Quit 
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "We'll define a quite value and then keep the 
    program running as long as the user has not entered the 
    quit value."

"""

prompt = "\tTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)