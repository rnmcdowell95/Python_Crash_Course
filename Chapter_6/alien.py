#Ryan McDowell
#Practicing using Python dictionaries
#7/6/21

# alien_o = {'color': 'green', 'points': 5}

# #print(alien_o['color'])
# #print(alien_o['points'])

# new_points = alien_o['points']
# print(f"You just scored {new_points} points!")

# print(alien_o)

# alien_o['x_position'] = 0
# alien_o['y_position'] = 25

# print(alien_o)

# print(f"The alien color is {alien_o['color']}!")
# alien_o['color'] = 'yellow'
# print(f"The alien color is {alien_o['color']}!")

# alien_o = {'x_position': 0, 'y_poisition': 25, 'speed': 'medium'}
# print(f"The position: {alien_o['x_position']}")

# #Move the alien to the right
# #Determine how far the alien moves based on its speed.
# if alien_o['speed'] == 'slow':
#     x_incremenet = 1
# elif alien_o['speed'] == 'medium':
#     x_incremenet = 2
# else:
#     #This is one fast alien!
#     x_incremenet = 3

# #The new position is the old position plus the increment
# alien_o['x_position'] = alien_o['x_position'] + x_incremenet

# print(f"The new position: {alien_o['x_position']}")

alien_o = {'color': 'green', 'points': 5}
print(alien_o)

#Removes the points key value pair
del alien_o['points']
print(alien_o)
