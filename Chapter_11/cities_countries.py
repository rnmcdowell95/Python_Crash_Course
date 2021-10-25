#Ryan McDowell
#10/02/2021
#Praticing testing functions in Python.

def city_country(city, country, population=''):

    if population:
        formatted_city_country = f"{city.title()}, {country.title()}, population - {population}"
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"

    return formatted_city_country

