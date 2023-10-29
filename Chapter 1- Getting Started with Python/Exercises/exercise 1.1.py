# Define the lines of the poem as strings.
line1 = "Twinkle, twinkle, little star,"
line2 = "    How I wonder what you are!"
line3 = "        Up above the world so high,"
line4 = "        Like a diamond in the sky."
line5 = "Twinkle, twinkle, little star,"
line6 = "    How I wonder what you are"

# Create an empty string to store the formatted poem.
poem = ""

# Add each line of the poem to the formatted string with proper indentation.
poem += line1 + "\n"  # Add the first line
poem += "\t" + line2 + "\n"  # Add the second line with one tab of indentation
poem += "\t\t" + line3 + "\n"  # Add the third line with two tabs of indentation
poem += "\t\t" + line4 + "\n"  # Add the fourth line with two tabs of indentation
poem += line5 + "\n"  # Add the fifth line
poem += "\t" + line6  # Add the sixth line with one tab of indentation

# Print the formatted poem.
print(poem)
