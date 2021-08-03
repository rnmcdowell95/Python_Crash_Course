#Ryan McDowell
#8/2/2021
#Practicing with Python functions that work with lists

# #Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot necklace', 'vase']
# printed_designs =[]

# #Simulate printing each design, until none are left.
# #Move each design to printed_designs after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing {current_design}.")
#     printed_designs.append(current_design)

# #Display all the printed models
# print("\nThe following items have been printed:")
# for design in printed_designs:
#     print(design)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing {current_design}.")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that have been printed."""
    print("\nThe following items have been printed:")
    for design in completed_models:
        print(design)

unprinted_designs = ['phone case', 'robot necklace', 'vase']
printed_designs =[]

print_models(unprinted_designs, printed_designs)
show_completed_models(printed_designs)