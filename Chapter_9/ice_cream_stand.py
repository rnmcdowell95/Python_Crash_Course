#Ryan McDowell
#8/10/21
#Practicing using class inheritance in Python

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

class Ice_Cream_Stand(Resturant):
    """Represent an ice cream stand simply."""

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = []
    
    def flavor_choice(self):
        """Defining what flavors are served at the ice cream stand."""

        print("Input ice cream flavors! Press q to stop when you are done.")
        flavor =''

        while flavor != 'q':
            flavor = input("What flavor should we add to the menu? ")
            self.flavors.append(flavor)

    def flavor_list(self):
        """Lists all of the flavors this ice cream stand serves."""
        for flavor in self.flavors:
            print(f"We serve {flavor.title()}!")

ice_cream_stand = Ice_Cream_Stand("McDowell's", "Ice Cream")

print(f"I run the {ice_cream_stand.name} ice cream stand!")

ice_cream_stand.flavor_choice()

ice_cream_stand.flavor_list()