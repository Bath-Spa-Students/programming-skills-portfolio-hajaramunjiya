# Create a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = [
    "tuna sandwich",
    "turkey sandwich",
    "vegetarian sandwich",
    "pastrami",
    "ham and cheese sandwich",
    "pastrami",
    "club sandwich",
    "pastrami"
]

# Create an empty list to hold finished sandwiches
finished_sandwiches = []

# Print a message if the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process each remaining sandwich order
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Remove the first order from the list
    print(f"I made your {current_order}.")  # Print a message for the current order
    finished_sandwiches.append(current_order)  # Add the current order to the finished_sandwiches list

# Print the list of finished sandwiches
print("\nList of sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
