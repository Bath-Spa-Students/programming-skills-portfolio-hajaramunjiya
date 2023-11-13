#Write a Python program that uses a function to check if a given number is prime or not

def is_prime(number):
    #the is_prime function takes a number as input and checks if it's prime or not
    """
    Check if a given number is prime.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any number in the range, it's not prime
        #If the number is divisible by any integer in that range, it's not prime; otherwise, it's considered prime

    return True  # If no divisor is found, the number is prime
#It iterates from 2 to the square root of the number, checking for divisibilit

# Example usage:
num_to_check = 17
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
#The function's call with a specified number is demonstrated in the sample use.