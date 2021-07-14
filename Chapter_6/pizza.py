#Ryan McDowell
#Practicing using lists in dictionaries
#7/8/21

#Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'pepperoni'],
    }

#Summarizing the order for the customer
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
