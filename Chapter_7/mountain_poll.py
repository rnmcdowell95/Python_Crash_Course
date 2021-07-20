#Ryan McDowell
#Practicing populating a dictionary with a user's input
#7/19/21

responses = {}

#Set a flag to indicate that pulling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Store the response in the dictionary.
    responses[name] = response
    
    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yet/no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")