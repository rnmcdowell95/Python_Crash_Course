#Ryan McDowell
#9/15/2021
#Practicing with reading text from other files


file_name = "cats.txt"

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} was not found")
else:
    print(f"These are cat types: {contents}")

file_name = "dogs.txt"
try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} was not found")
else:
    print(f"These are dog types: {contents}")