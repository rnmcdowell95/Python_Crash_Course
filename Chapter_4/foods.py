#Ryan McDowell
#List practice copying
#6/29/21

my_foods = ['pizza', 'asam laksa', 'char kwe teoy']
friends_food = my_foods [:]

my_foods.append('cheese')
friends_food.append('durian')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

for food in my_foods[:3]:
    print(food)