# List of people to invite to dinner
invitees = ['Leonardo da Vinci', 'Marie Curie', 'Nelson Mandela']
#We have a list of people to invite to dinner stored in the invitees variable.

# Print invitation messages
for person in invitees:
    invitation_message = f"Dear {person},\nYou are cordially invited to dinner at my place. It would be an honor to have you join us."
    print(invitation_message)
    print()  # Add an empty line for separation between invitations
#The for loop iterates through each person in the list.

#Inside the loop, we create a personalized invitation message using an f-string for each person.

#We print each invitation message, inviting each person to dinner.