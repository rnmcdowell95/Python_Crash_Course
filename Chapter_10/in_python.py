#Ryan McDowell
#8/13/21
#Practicing reading from a file.

file_name = "in_python.txt"

lines = []

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in file_object:
        print(line)
    

for line in lines:
    print(f"{line.strip()}")
    