#Ryan McDowell
#10/02/2021
#Practicing writing test cases for Python functions.

import unittest
from cities_countries import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'cities_countries.py'."""

    def test_city_country(self):
        """Does a city like 'Georgetown' and a country like "Malaysia' work?"""
        city_and_country = city_country('georgetown', 'malaysia')
        self.assertEqual(city_and_country, 'Georgetown, Malaysia')

if __name__ == '__main__':
    unittest.main()