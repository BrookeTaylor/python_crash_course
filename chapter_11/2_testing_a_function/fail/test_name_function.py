"""

    Title: Testing a Function continued.
    Author: Eric Matthes
    Date: 04/24/2023
    Description: "Before we run the test, let's take a closer look at this 
    function. The name of a test file is important; it must start with test_. 
    When we ask pytest to run the tests we've written, it will look for any 
    file that begins with test_, and run all of the tests it finds in that 
    file."

"""

from name_function_fail import get_formatted_name

def test_first_last_name():

    # Do names like 'Janis Joplin work?
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

