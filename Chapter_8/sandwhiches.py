#Ryan McDowell
#8/5/21
#Practicing working with a function that accepts an arbitrary number of arguments.

def make_sandwiches(*ingredients):
    print("\nMaking a sandwhich with the following ingredeints:")
    for ingredient in ingredients:
        print(f"{ingredient}")

make_sandwiches('turkey', 'bolagna', 'cheese', 'ham')