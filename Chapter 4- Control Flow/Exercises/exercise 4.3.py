# Choose a color for the alien, you can change this value to test different scenarios
alien_color = 'yellow'  # You can change this to 'green' or 'red' to test different colors

# This is the first version of the program where the alien is green.
if alien_color == 'green':
    # If the alien is green, print a message that the player earned 5 points.
    print("Player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    # If the alien is yellow, print a message that the player earned 10 points.
    print("Player just earned 10 points for shooting the yellow alien.")
else:
    # If the alien is not green or yellow, it must be red, so print a message that the player earned 15 points.
    print("Player just earned 15 points for shooting the red alien.")
# The if-elif-else chain ends here.

# This is the second version of the program where the alien is yellow.
alien_color = 'yellow'  # Change the alien's color to 'yellow'

# Re-run the same if-elif-else chain to check the new alien_color.
if alien_color == 'green':
    # This block won't be executed since the alien_color is not green.
    print("Player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    # This block will be executed since the alien_color is yellow.
    print("Player just earned 10 points for shooting the yellow alien.")
else:
    # This block won't be executed since the alien_color is not red.
    print("Player just earned 15 points for shooting the red alien.")
# The if-elif-else chain ends here, and in this version, the 'elif' block is executed.

# This is the third version of the program where the alien is red.
alien_color = 'red'  # Change the alien's color to 'red'

# Re-run the same if-elif-else chain to check the new alien_color.
if alien_color == 'green':
    # This block won't be executed since the alien_color is not green.
    print("Player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    # This block won't be executed since the alien_color is not yellow.
    print("Player just earned 10 points for shooting the yellow alien.")
else:
    # This block will be executed since the alien_color is red.
    print("Player just earned 15 points for shooting the red alien.")
# The if-elif-else chain ends here, and in this version, the 'else' block is executed.

#In each version of the program, the appropriate message is printed based on the color of the alien.