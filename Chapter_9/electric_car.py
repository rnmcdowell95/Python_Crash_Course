#Ryan McDowell
#8/6/21
#Creaing a module to practice importing from another module

"""A Class that can be used to represent an electric car."""

from car import Car

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


class Electric_Car(Car):
    """"Represents all things relevant to an electric car."""

    def __init__(self, make, model, year):
        """Initializing the attributes for an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()    
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks!"""
        print("This car doesn't need a gas tank!")


