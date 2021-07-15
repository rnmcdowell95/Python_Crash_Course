#Ryan McDowell
#Practicing manipulating lists and dictionaries with loops.
#7/14/21


#Start with the users that need to berified and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'bronco', 'bob']
confirmed_users = []

#Verify each user until there are no more uncofirmed users. Move each verified user into the list of confirmed users.
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print(f"Verifying user: {confirmed_user.title()}")
    confirmed_users.append(confirmed_user)

#Display all of the confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())