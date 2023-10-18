#Compute the area of a triangle 

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Input the values of base and height from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = calculate_triangle_area(base, height)

# Display the result
print(f"The area of the triangle with base {base} and height {height} is {area}")

#We define a function calculate_triangle_area that takes the base and height as parameters and returns the area.

#We input the values of the base and height from the user.

#We call the calculate_triangle_area function with the input values to calculate the area.

#Finally, we print the result, displaying the calculated area of the triangle