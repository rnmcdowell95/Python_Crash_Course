#Ryan McDowell
#8/6/21
#Creaing a module to import classes.

"""A Class that can be used to represent a car."""


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


