#Ryan McDowell
#8/5/21
#Practicing functions that take an arbitrary amount of argument pairs.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='prinston', field='physics')

print(user_profile)