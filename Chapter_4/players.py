#Ryan McDowell
#Slicing a list practice
#6/29/21

players = ['kyle', 'daniel', 'bronco', 'andy', 'ryan', 'jose']
print(players[0:3])
print(players[2:])

print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())