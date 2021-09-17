#Ryan McDowell
#9/15/2021
#Practicing storing User inputs in JSON format

import json

username = input("Enter your username: ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"Thanks for submitting your name, we'll be ready for you when come back {username}!")