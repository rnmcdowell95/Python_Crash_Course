#Ryan McDowell
#Practicing with lists and loops
#6/29/21

numbers = []
#Printing the numbers 1-20 inclusive wiht a list
for number in range(1,21):
    numbers.append(number)
print(numbers)


# #Print 1-1mil
# for number in range(1,1000001):
#     print(number)
numbers = []
#Printing the odd numbers 1-20
for number in range(1, 21, 2):
    numbers.append(number)
print(numbers)

numbers = []
#Printing the numbers that are a multiple of 3 
for number in range(3,31,3):
    numbers.append(number)
print(numbers)

numbers = []
#Printing the numbers that are a multiple of 3 
for cube in range(1,11):
    print(cube**3)

numbers = [cube**3 for cube in range(1,11)]
print(numbers)