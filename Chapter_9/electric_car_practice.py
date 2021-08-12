#Ryan McDowell
#8/6/21
#Practicing with Python class inhert.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_description(self):
        """Return a neatly formatted descriptive name for the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Prints the amount of miles the car has traveled."""
        print(f"This car has traveled {self.odometer_reading} miles.")

    def update_odometer(self, mileage):
        """
        Updates the odometer reading.
        Rejects the attempt to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer back!")

    def incremenet_odometer(self, mileage):
        """Adds the miles driven to the odoemter."""
        if mileage >= 0:
            self.odometer_reading += mileage
        else:
            print("You can't roll the odometer back!")

    def fill_gas_tank(self):
        """Filling the gas tank of a car."""
        print("The gas tank has been filled up!")


class Battery:
    """A simple representation of a battery."""

    def __init__(self, battery_size = 75):
        """Initilize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery's size."""
        print(f"This cas has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """"Represents all things relevant to an electric car."""

    def __init__(self, make, model, year):
        """Initializing the attributes for an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()    
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks!"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_description())

my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()