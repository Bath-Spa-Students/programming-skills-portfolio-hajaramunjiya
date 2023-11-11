# Initialize a flag variable to control the loop
continue_purchase = True

# Start a loop to continue asking for ages until the user decides to stop
while continue_purchase:
    # Ask the user for their age
    age = input("Please enter your age (or type 'quit' to exit): ")
#We use a while loop to repeatedly ask the user for their age until they decide to exit by typing 'quit

    # Check if the user wants to exit
    if age.lower() == 'quit':
        continue_purchase = False
        break

    # Convert the user input to an integer
    age = int(age)
#We ask the user for their age using the input function and then convert the input to an integer

    # Determine the ticket price based on age
    if age < 3:
        ticket_price = "Free"
    elif 3 <= age <= 12:
        ticket_price = "$10"
    else:
        ticket_price = "$15"
#We determine the ticket price based on the user's age according to the provided conditions.

    # Display the cost of the movie ticket
    print(f"Based on your age of {age}, the cost of your movie ticket is {ticket_price}.\n")
#We display the cost of the movie ticket for each user.
#The loop continues until the user decides to exit.

# End the program with a message
print("Thank you for using our movie ticket service!")
