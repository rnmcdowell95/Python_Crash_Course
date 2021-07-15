#Ryan McDowell
#Using a while loop to iterate through a list and remove all instances of a particular item
#7/14/21

pets = ['dog', 'cat', 'dog', 'goldish', 'cat', 'dog', 'rabbit']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)