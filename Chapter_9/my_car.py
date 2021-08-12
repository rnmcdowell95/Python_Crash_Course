#Ryan McDowell
#8/10/21
#Practicing importing classes using a module.

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_description())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
