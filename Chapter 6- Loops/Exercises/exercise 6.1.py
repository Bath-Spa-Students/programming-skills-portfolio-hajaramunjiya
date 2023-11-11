# Initialize an empty list to store the pizza toppings
pizza_toppings = []

while True:
    # Prompt the user to enter a topping
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    # Add the topping to the list
    pizza_toppings.append(topping)

    # Print a message adding the topping with large comments
    print("\nAdding", topping, "to your pizza!\n")

# Display the final list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("-", topping)
