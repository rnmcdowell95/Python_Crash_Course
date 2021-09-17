#Ryan McDowell
#9/16/2021
#Practicing reading input from a JSON file that a user had generated.

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}!")