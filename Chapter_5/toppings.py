#Ryan McDowell
#Practicing comparisons using pizza
#7/6/21

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17

if answer != 42:
    print("That is not the correct answer!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("This man getting some shrooms.")

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'cheese' in requested_toppings:
    print("Adding cheese.")
if 'onions' in requested_toppings:
    print("Adding onions")

for topping in requested_toppings:
    if topping == "pineapple":
        print("Sorry, we are out of pineapple right now.")
    else:
        print(f"Adding {topping}!")

print("\nFinishing making your pizza.")

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['cheese', 'pepperoni', 'pineapple', 'green pepper', 'canadian bacon', 'olives']

requested_toppings = ['cheese', 'pineapple', 'canadian bacon', 'sausage']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping} to your pizza!")
    else:
        print(f"Sorry, we do not have {topping} in stock.")

print("\nYour pizza is now ready.")
