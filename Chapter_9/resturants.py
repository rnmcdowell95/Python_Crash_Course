#Ryan McDowell
#8/6/21
#Practicing using classes in Python

print('Test')

class Resturant:
    """A model of a resturant for practice."""

    def __init__(self, name, cuisine):
        """Initializes a resturant with a name and cuisine it serves."""
        self.name = name
        self.cuisine = cuisine
    
    def description(self):
        """Prints a generic description of the resturant."""
        print(f"Come eat at {self.name}, our fantastic generic resturant!")

    def food(self):
        """Prints out what sort of food is served at the resturant"""
        print(f"At {self.name} we serve {self.cuisine}!")

my_resturant = Resturant('McDowell', 'melts')

print(f"{my_resturant.name}")
my_resturant.cuisine

my_resturant.description()
my_resturant.food()