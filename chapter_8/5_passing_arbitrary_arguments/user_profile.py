"""

    Title: Using Arbitrary Keyword Arguments
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "Sometimes you'll want to accept an arbitrary number 
    of arguments, but you won't know ahead of time what kind of 
    information will be passed to the function. In this case, you can 
    write functions that accept as many key-value pairs as the calling 
    statement provides. One example involves building user profiles: 
    you know you'll get information about a user. but you're not sure 
    what kind of information you'll receive. The function 
    build_profile() in the following example always takes in a first 
    and last name, but it accepts an arbitrary number of keyword 
    arguments as well:"

"""
def build_profile(first, last, **user_info):

    # Build a dictionary containing everything we know about a user.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location= 'princeton',
                             field= 'physics')

print(user_profile)