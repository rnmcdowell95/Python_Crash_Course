#Ryan McDowell
#9/15/2021
#Practicing reading information from a JSON formatted file

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)