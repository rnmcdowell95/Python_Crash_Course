#Ryan McDowell
#8/5/2021
#Practicing with Python functions that work with an arbitrary number of arguments.

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(5, 'cheese',)
make_pizza(7, 'cheese', 'pineapple', 'basil')