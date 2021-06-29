#Ryan McDowell
#Manipulating lists for practice
#6/28/21

destinations = ['penang', 'japan', 'washington d. c.', 'the british isles', 'rome']

#Showing List and temp sorting alphabetically
print(destinations)
print(sorted(destinations))

#Showing list is still the same and then temp sorting reverse alphabetically
print(destinations)
print(sorted(destinations, reverse=True))
print(destinations)

#Reverseing the list
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)

#sorting permanently
destinations.sort()
print(destinations)
destinations.sort(reverse=True)
print(destinations)



