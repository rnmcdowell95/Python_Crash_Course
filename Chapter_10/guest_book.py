#Ryan McDowell
#8/13/21
#Practicing with writing to files in Python.

file_name = 'guest_book.txt'
guest = ''

with open(file_name, 'a') as file_object:
    while guest != 'q':
        guest = input("What is the name of the guest staying with us today? (Please input 'q' to exit the program) ")
        if guest =='q':
            break
        else:
            file_object.write(f"{guest}\n")
