#Ryan McDowell
#10/02/2021
#Practicing with testing in Python

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Ryan Nathaniel Loh' work?"""
        formatted_name = get_formatted_name('ryan', 'loh', 'nathaniel')
        self.assertEqual(formatted_name, 'Ryan Nathaniel Loh')

if __name__ == '__main__':
    unittest.main()