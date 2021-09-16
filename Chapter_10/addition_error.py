#Ryan McDowell
#8/24/21
#Practicing error handling with numbers

from typing import cast


print("Hello! Please provide two numbers that you would like to add together.")

first_number = input("Please provide the first number: ")
second_number = input("Please provide the second number: ")


try:
    first_number = int(first_number)
    second_number = int(second_number)
    divsion = first_number + second_number
    
except ZeroDivisionError:
    print("You can't divide by 0!")
except ValueError:
    print("Please enter an integer value.")
else:
    print(f"{first_number}+{second_number} = {divsion}")