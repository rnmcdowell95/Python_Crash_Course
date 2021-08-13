#Ryan McDowell
#8/13/21
#Practicing writing to a file in Python.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I want to be better at Python.\n")
    file_object.write("I want a second line.\n")