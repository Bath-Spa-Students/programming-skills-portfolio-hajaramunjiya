# Create a list to store the names of friends
names = ['asmina', 'naja', 'haya', 'aisha', 'eva']

# Use a for loop to access and print each person's name one at a time
for i in range(len(names)):
    # Access the current name using the index 'i'
    current_name = names[i]
    
    # Print each person's name one at a time
    print(f"Friend {i + 1}: {current_name}")

# Alternatively, you can also iterate through the list directly without using an index
print("\nUsing a for loop to directly access each person's name:")
for name in names:
    print(name)

# You can also use a while loop to achieve the same result
print("\nUsing a while loop to access and print each person's name:")
i = 0
while i < len(names):
    current_name = names[i]
    print(f"Friend {i + 1}: {current_name}")
    i += 1
