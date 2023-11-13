#Write a Python program that uses a while loop to find the largest number among a series of user-input values until they enter '0' to exit the loop.

# Initialize a variable to store the largest number
largest_number = float('-inf')

# Prompt the user for input
while True:
    user_input = input("Enter a number (enter '0' to exit): ")
    #the while loop continues until the user enters '0'.

    # Check if the user wants to exit the loop
    if user_input == '0':
        break

    try:
        # Convert the input to a float
        number = float(user_input)

        # Update the largest number if the current number is larger
        if number > largest_number:
            largest_number = number
            #nside the loop, the program prompts the user for a number, converts the input to a float, and updates the largest_number variable if the current number is larger.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        #If the user enters an invalid input, a ValueError is caught, and the program prompts the user to enter a valid number.

# Display the result
if largest_number != float('-inf'):
    print("The largest number entered is:", largest_number)
else:
    print("No valid numbers entered.")
    #Once the user enters '0', the loop exits,
