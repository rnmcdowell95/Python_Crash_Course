#Ryan McDowell
#More list practice with a guest book theme
#6/28/21

guests = ['Jesus', 'Gandalf', 'Guts']
print(f"Hello {guests[0]}, my lord and savior! I am having a dinner party tomorrow night and would love for you to come. Please let me know if you are able to make it.")
print(f"I am glad to see you are still wearing the white {guests[1]}. I hope you can join me for this expected dinner party I am having tomorrow!")
print(f"Hi {guests[2]} since you have have al ot of free time now would you want to come to my dinner party?")

print(f"Sadly {guests[2]} was not able to make it to the dinner party")

guests.remove('Guts')
guests.append('Ginger')

print(f"Hi, {guests[0]}! I just wanted to let you know we had a change in our guest list but the dinner party is still on for tomorrow.")
print(f"{guests[1]}, there was a change in the guest list. Don't bring dwarves with you though.")
print(f"Hi my sweet doggy {guests[-1]} I look forward to you being at dinner.")

