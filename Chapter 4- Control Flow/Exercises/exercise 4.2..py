# Choose a color for the alien, you can change this value to test different scenarios
alien_color = 'yellow'  # You can change this to 'green' to run the 'if' block

# Write an if-else chain to check the color of the alien.
if alien_color == 'green':
    # If the alien's color is green, print a statement that the player just earned 5 points.
    print("Player just earned 5 points for shooting the green alien.")
else:
    # If the alien's color isn't green, print a statement that the player just earned 10 points.
    print("Player just earned 10 points for shooting the alien that isn't green.")
# The if-else chain ends here.

# Now, let's create a version of the program where the 'if' block is executed.
alien_color = 'green'  # Change the alien's color to 'green'

# Re-run the same if-else chain to check the new alien_color.
if alien_color == 'green':
    # This 'if' block will be executed since the alien_color is 'green'.
    print("Player just earned 5 points for shooting the green alien.")
else:
    # This 'else' block won't be executed since the alien_color is 'green'.
    print("Player just earned 10 points for shooting the alien that isn't green.")
# The if-else chain ends here, and in this version, the 'if' block is executed.
