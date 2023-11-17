# Initial list of guests
guests = ['Aazra', 'ilsa', 'aisha', 'naima']

# Print a message about the limit of guests
print("Due to a delay, the new dinner table won't arrive in time. You can only invite two people for dinner.")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to the two remaining guests
for remaining_guest in guests:
    print(f"{remaining_guest}, you're still invited to dinner.")

# Use del to remove the last two names from the list
del guests[:]

# Print the empty list to confirm
print("The final guest list is:", guests)
