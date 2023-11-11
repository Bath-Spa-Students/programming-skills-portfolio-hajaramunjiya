# Create a list of sandwich orders
sandwich_orders = ["Ham and Cheese", "Turkey Club", "beef", "Tuna", "Chicken Salad"]

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop()  
    # Get the last order from the list

# Make the sandwich and print a message
    print(f"I made your {current_order} sandwich.")
    
    # Add the finished sandwich to the finished_sandwiches list
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
    
    