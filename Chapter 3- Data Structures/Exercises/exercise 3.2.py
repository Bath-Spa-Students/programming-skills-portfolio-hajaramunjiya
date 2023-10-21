# Create a list of friends' names
friend_names = ['Asmina', 'naja', 'thahliya', 'fara']

# Define the common message to personalize
message = "Hello, {}! I wanted to let you know how much I appreciate your friendship."

# Iterate through the list of names and print personalized messages
for name in friend_names:
    # Personalize the message with the current friend's name
    personalized_message = message.format(name)
    
    # Print the personalized message
    print(personalized_message)

# Alternatively, you can also use a list comprehension for brevity
personalized_messages = [message.format(name) for name in friend_names]

# Print the personalized messages
print("\nPersonalized Messages (Using List Comprehension):")
for msg in personalized_messages:
    print(msg)
#We also demonstrate how you can achieve the same result using list comprehension, where we generate a list of personalized messages and print them in a loop