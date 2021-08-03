#Ryan McDowell
#8/2/2021
#Practicing with Python functions that work with lists

def greet_users(names):
    """A function that works through a list of names and greets each one."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['jade', 'bob', 'kyle', 'jack']
greet_users(usernames)