# List of people to invite to dinner
invitees = ['Leonardo da Vinci', 'Marie Curie', 'Nelson Mandela']
#We start with the initial invitation messages and print them

# Print invitation messages
print("Initial Invitation Messages:")
for person in invitees:
    invitation_message = f"Dear {person},\nYou are cordially invited to dinner at my place."
    print(invitation_message)
    print()  # Add an empty line for separation between invitations
#We simulate a guest not being able to make it and print their name.

# Simulate a guest not being able to make it
guest_not_available = invitees.pop(1)
print(f"\nUnfortunately, {guest_not_available} can't make it to the dinner.\n")
#We replace the guest who can't make it with a new guest (Isaac Newton).

# Replace the guest who can't make it with a new guest
invitees.append('Isaac Newton')

# Print updated invitation messages
print("Updated Invitation Messages:")
for person in invitees:
    invitation_message = f"Dear {person},\nYou are cordially invited to dinner at my place."
    print(invitation_message)
    print()  # Add an empty line for separation between invitations
#We print the updated invitation messages with the new guest included
