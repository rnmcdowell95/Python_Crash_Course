#Ryan McDowell
#Practicing nesting dictionaries and accessing them in Python
#7/13/21

cities = {
    'george town': {
        'population': 700000,
        'country': 'malaysia',
        'fact': 'Home of Penang Asam Laksa!'
    },
    'seatle': {
        'population': 4000000,
        'country': 'united states',
        'fact': 'Is in the Pacific Northwest.'
    },
    'london': {
        'population': 18000000,
        'country': 'united kingdoms',
        'fact': 'London was once a Roman fort.'
    }

}

for city, city_info in cities.items():
    print(f"Today we are talking about {city.title()}!")

    population = city_info['population']
    country = city_info['country']
    fact = city_info['fact']

    print(f"\t{city.title()} has a population of {population} people.")
    print(f"\t{city.title()} is located in {country.title()}.")
    print(f"\tHere is a fun fact about {city.title()}: {fact}.")