#Ryan McDowell
#8/3/2021
#Practicing function value returns


#Original piece of code used to display a formatted first and last name that is supplyed
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('jim', 'smith', 'bob')
# print(musician)

#Infinite loop ahead!
while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' at any time to quit.")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name (f_name, l_name)
    print(formatted_name)