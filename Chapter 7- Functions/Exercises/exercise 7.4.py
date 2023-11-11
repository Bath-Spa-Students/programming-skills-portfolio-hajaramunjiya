def make_shirt(size="Large", message="free palestine"):
    """Prints a sentence summarizing the size and message on the shirt."""
    print(f"Shirt size: {size}, Message: {message}")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a custom-sized shirt with a different message
make_shirt(size="Small", message="free palestine")
