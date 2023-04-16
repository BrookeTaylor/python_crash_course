"""

    Title: Defining a Function
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "The first line uses the keyword def to inform
    Python that you're defining a function. The is the function 
    definition, which tells Python the name of the function and, if 
    applicable, what kind of information the function needs to do 
    it's job. The parentheses hold that information."

"""
def greet_user():

# Display a simple greeting.
    print("Hello")

#   A function call tells Python to execute the code in the function. 
#   To call a function, you write the name of the function, followed 
#   by necessary information in parentheses. 
greet_user()





"""

    Title: Passing Information to a Function
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "By adding username here, you allow the function to 
    accept any value of username you specify. The function now 
    expects you to provide a value for username each time 
    you call it."

"""
def greet_users(username):
    print(f"Hello, {username.title()}!")

greet_users('Brooke')


"""

    Arguments and Parameters

    "Once we called the function and gave it the information 
    (a person's name), it printed the right greeting.

    The variable username in the definition of greet_users() is 
    an example of a parameter, a piece of information the function 
    needs to do its job. An argument is a piece of information that's 
    passed from a function call to a function.
    
    In this case the argument 'Brooke'
    was passed to the function greet_users(),
    and the value was assigned to the parameter username."

"""

