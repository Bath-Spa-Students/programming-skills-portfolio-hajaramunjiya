def make_shirt(size, message):
    """Prints a sentence summarizing the size and message on the shirt."""
    print(f"Shirt size: {size}, Message: {message}")

# Call the function using positional arguments
make_shirt("Medium", "mickey mouse")

# Call the function using keyword arguments
make_shirt(size="Large", message="bla blah blah")
