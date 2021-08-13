#Ryan McDowell
#8/13/21
#Practicing working with Python errors.

file_name = 'alice.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist.")