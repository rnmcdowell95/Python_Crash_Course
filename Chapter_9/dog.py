#Ryan McDowell
#8/5/21
#Creating a class to represent dogs

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """"Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Ginger', 1)
my_other_dog = Dog('Pepper', 1)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

my_other_dog.sit()