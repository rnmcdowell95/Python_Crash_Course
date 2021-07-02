#Ryan McDowell
#Lists and loops practice
#6/29/21

#Starter for creating a list of squares of numbers 1-10
squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

#A more efficient way to create the list of squares of numbers 1-10
squares = []

for value in range(1,11): 
    squares.append(value ** 2)

print(squares)

#An even more efficient way to create the list of squares of numbers 1-10 using a list comprhension

squares = [value**2 for value in range(1,11)]
print(squares)