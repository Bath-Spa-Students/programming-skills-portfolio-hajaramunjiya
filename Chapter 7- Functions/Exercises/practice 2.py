#Write a Python function that calculates the factorial of a given positive integer using recursion.

def factorial(n):
    """
    Recursive function to calculate the factorial of a positive integer.

    Parameters:
    n (int): The positive integer for which factorial is to be calculated.

    Returns:
    int: The factorial of the input integer.
    """
    #the factorial function is defined recursively.

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)
#it has a base case for when n is 0, in which case it returns 1. 

#it recursively calls itself with (n-1) and multiplies the result by n


# Example usage:
#The following example explains how to use the function with a given number.
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
