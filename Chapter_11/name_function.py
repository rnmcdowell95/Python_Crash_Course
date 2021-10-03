#Ryan McDowell
#9/29/2021
#Practicing testing code


def get_formatted_name(first, last, middle=''):
    """Generates a neatly formatted name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
