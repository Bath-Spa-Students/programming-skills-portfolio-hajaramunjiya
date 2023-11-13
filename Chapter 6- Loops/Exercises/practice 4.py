#Write a Python program that uses the break statement to exit a for loop when a specific condition is met

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize a variable to store the target number
target_number = 5

# Use a for loop to iterate through the numbers
for number in numbers:
    #the for loop iterates through the list of numbers
    print("Current number:", number)

    # Check if the current number is the target number
    if number == target_number:
        #The loop checks if the current number is equal to the target_number
        print("Target number found! Exiting the loop.")
        break
# If the condition is met, the break statement is executed, which exits the loop

# This statement will be executed after the loop
print("Loop finished.")
