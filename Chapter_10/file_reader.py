#Ryan McDowell
#8/12/21
#Practicing reading data from a file

file_name = 'pi_digits.txt'

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip()e)

# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())