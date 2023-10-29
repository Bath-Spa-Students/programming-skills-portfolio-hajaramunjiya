import math

# Prompt the user to input the radius of the circle.
# The input function reads a line of text from the user and converts it to a float (decimal number).
radius = float(input("Please enter the radius of the circle: "))

# Define the value of pi. We'll use the math module for this purpose.
import math

# Calculate the area of the circle using the formula: Area = π * r^2
# π (pi) is a constant provided by the math module.
# r is the radius provided by the user.
area = math.pi * (radius ** 2)

# Print the calculated area of the circle.
print(f"The area of the circle with radius {radius} is {area:.2f}")
# The ":.2f" inside the f-string formats the result to two decimal places for a more user-friendly output.
