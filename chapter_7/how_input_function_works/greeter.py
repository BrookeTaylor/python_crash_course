"""

    Title: How the input() Function Works 
    Author: Eric Matthes
    Date: 04/07/2023
    Description: "Sometimes you'll want to write a prompt that's 
    longer than one line For example, you might want to tell the 
    user why you're asking for certain input. You can assign 
    your prompt to a variable and pass that variable to the 
    input() function. This allows you to build your prompt over 
    several lines, then write a clean input() statement."

"""

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")