#Ryan McDowell
#Practicing user input and while loops
#7/14/21

prompt = "\nTell me something, and I will repeate it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ''

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
