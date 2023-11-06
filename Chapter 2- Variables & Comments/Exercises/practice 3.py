# Prompt the user for input
user_input = input("Enter a value: ")
#the user is prompted to enter a value, and the input is typecast to a string, int, and float

# Typecast the input to string
input_as_string = str(user_input)

# Typecast the input to integer
try:
    input_as_int = int(user_input)
except ValueError:
    input_as_int = None  # Handle the case where the input cannot be converted to an integer

# Typecast the input to float
try:
    input_as_float = float(user_input)
except ValueError:
    input_as_float = None  # Handle the case where the input cannot be converted to a float
#Appropriate error handling is provided for cases where the input cannot be converted to an integer or a float

# Print the variables with comments
print("User Input as String:", input_as_string)
print("User Input as Integer:", input_as_int)
print("User Input as Float:", input_as_float)
