#Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius

import math

def calculate_circle_area(radius):
 #the calculate_circle_area function takes the radius as input and uses the formula πr2 to calculate the area of the circle
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    area = math.pi * radius**2
    return area
#The math.pi constant is used for the value of pi. 

# Example usage:
radius = 6.0
area_of_circle = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {area_of_circle}")
#The following example shows how to use the function with a given number.
