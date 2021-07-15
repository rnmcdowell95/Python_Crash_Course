#Ryan McDowell
#Determing if a user's input is even or odd using the modulo operator.
#7/14/21

number = input("Enter a number, and I'll tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")