#Ryan McDowell
#10/25/2021
#Writing test cases for the employee class.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an employee class to test with."""

        first_name = 'ryan'
        last_name = 'toot'
        salary = 75000

        self.my_employee = Employee(first_name, last_name, salary)
    
    def test_give_default_raise(self):
        """Test giving the default raise amount to the employee."""
        self.my_employee.give_raise()
        self.assertEqual(80000, self.my_employee.salary)

    def test_give_custom_raise(self):
        """Test giving a custom raise amount to the employee"""
        custom_raise = 8000
        self.my_employee.give_raise(custom_raise)
        self.assertEqual(83000, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()
