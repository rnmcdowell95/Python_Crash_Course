#Ryan McDowell
#Practicing nesting dictionaries
#7/8/21

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'chadb': {
        'first': 'chad',
        'last': 'brunswick',
        'location': 'arizona',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")