#Ryan McDowell
#9/15/2021
#Practicing storing data in JSON.

import json

numbers = [2, 3, 4, 5, 6, 7]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)