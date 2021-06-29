#Ryan McDowell
#Organizing lists
#6/28/21

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)

cars.reverse()
print(cars)
car_length = len(cars)
print(car_length)