"""

    Title: Modifying a List in a Function 
    Author: Eric Matthes
    Date: 04/15/2023
    Description: "When you pass a list to a function, the function can 
    modify the list. Any changes made to the list inside the 
    function's body are permanent, allowing you to work efficiently 
    even when you're dealing with large amounts of data.
    
    Consider a company that creates 3D printed models of designs that 
    users submit. Designs that need to be printed are stored in a 
    list, and after being printed they're moved to a separate list. 
    The following code does this without using functions:"

"""
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


"""

    "This program starts with a list of designs that need to be 
    printed and an empty list called completed_models that each design 
    will be moved to after it has been printed. As long as designs 
    remain in unprinted_designs, the while loop simulates printing 
    each design by removing a design from the end of the list, storing 
    it in current_design, and displaying a message that the current 
    design is being printed. It then adds the design to the list of 
    completed models. When the loop is finished running, a list of the 
    designs that have been printed is displayed:"

"""