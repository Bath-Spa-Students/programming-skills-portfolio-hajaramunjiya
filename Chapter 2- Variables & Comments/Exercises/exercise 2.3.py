# Define the person's name with whitespace at the beginning and end
person_name = "\t \n hajara ishaq\n \t"

# Print the name with whitespace around it
print(f"Original Name: '{person_name}'")

# Use lstrip() to remove whitespace from the left side
left_stripped_name = person_name.lstrip()
print(f"Left Stripped Name: '{left_stripped_name}'")

# Use rstrip() to remove whitespace from the right side
right_stripped_name = person_name.rstrip()
print(f"Right Stripped Name: '{right_stripped_name}'")

# Use strip() to remove whitespace from both sides
fully_stripped_name = person_name.strip()
print(f"Fully Stripped Name: '{fully_stripped_name}'")
