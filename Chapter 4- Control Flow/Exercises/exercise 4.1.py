# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color = 'green'  # You can change this value to test different scenarios

# Write an if statement to test whether the alien’s color is green.
if alien_color == 'green':
    # If the alien's color is green, print a message that the player just earned 5 points.
    print("Player just earned 5 points.")
# The if statement ends here.

# Now, let's create a version of the program where the if test fails (no output).
alien_color = 'red'  # Change the alien's color to 'red'

# Write the same if statement to test whether the alien's color is green.
if alien_color == 'green':
    # This block will only execute if the alien_color is 'green', which is not the case here.
    print("Player just earned 5 points.")
# The if statement ends here, but there's no output because the test failed.
