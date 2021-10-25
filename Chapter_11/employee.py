#Ryan McDowell
#10/25/2021
#Practice with Classes and self testing.

class Employee:

    def __init__(self, first_name, last_name, salary):
        """Initialize an employee with their basic information."""

        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def give_raise(self, custom_raise =''):
        print(f"{self.first_name.title()}'s salary is currently: {self.salary}")
        
        if custom_raise:
            self.salary = self.salary + int(custom_raise)
            print(f"{self.first_name.title()} has received a raise! Their salary is now: {self.salary}")
        else:
            self.salary = self.salary + 5000
            print(f"{self.first_name.title()} has received a raise! Their salary is now: {self.salary}")
    
    
            