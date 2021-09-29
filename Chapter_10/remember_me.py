#Ryan McDowell
#9/15/2021
#Practicing storing User inputs in JSON format

import json

#Load the username, if it has been stored previously
#Otherwise, prompt for the username and store it.

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Get a new username."""
    username = input("Enter your username: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)

    return username


def greet_user():
    """Greet the user by name."""
    
    username = get_stored_username()
    
    

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"Thanks for submitting your name, we'll be ready for you when come back {username}!")

        
greet_user()