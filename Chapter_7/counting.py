#Ryan McDowell
#Practicing using while loops and continue in loops
#7/14/21

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)