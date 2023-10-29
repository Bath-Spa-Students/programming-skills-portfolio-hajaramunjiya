# Set a value for the variable age, you can change this value to test different scenarios
age = 30  # You can change this to any age to determine the person's stage of life

# Check the person's stage of life based on their age.
if age < 2:
    # If the person is less than 2 years old, print a message that the person is a baby.
    print("The person is a baby.")
elif age < 4:
    # If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
    print("The person is a toddler.")
elif age < 13:
    # If the person is at least 4 years old but less than 13, print a message that the person is a kid.
    print("The person is a kid.")
elif age < 20:
    # If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
    print("The person is a teenager.")
elif age < 65:
    # If the person is at least 20 years old but less than 65, print a message that the person is an adult.
    print("The person is an adult.")
else:
    # If the person is age 65 or older, print a message that the person is an elder.
    print("The person is an elder.")
# The if-elif-else chain ends here.
