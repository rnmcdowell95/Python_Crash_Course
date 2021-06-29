#Ryan McDowell
#Practicing manipulating lists in Python.
#6/28/21

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
message = f"The last motorcycle I bought was a {popped_motorcycle.title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"{too_expensive.title()} was too expensive for me becaue I'm a peasant.")