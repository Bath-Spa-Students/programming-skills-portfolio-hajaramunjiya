#Write a Python program that defines a function to check whether a given number is prime

def is_prime(number):
    #the is_prime function takes an integer as input and checks whether it's a prime number
    """
    Check if a given number is prime.

    Parameters:
    number (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    #uses a basic primality check by iterating from 3 to the square root of the number and checking for divisibility

    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check for divisibility from 3 to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Example usage:
num_to_check = 23
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
