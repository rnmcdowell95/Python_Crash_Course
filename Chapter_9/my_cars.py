#Ryan McDowell
#8/11/21
#Practicing importing multiple modules

# from car import Car, Electric_Car

from car import Car
from electric_car import Electric_Car as EC

my_honda = Car('honda','accord', 1991)
print(my_honda.get_description())

my_tesla = EC('Tesla', 'Model y', 2021)
print(my_tesla.get_description())