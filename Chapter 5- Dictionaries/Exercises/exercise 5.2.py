# Create a glossary dictionary with programming words and their meanings
glossary = {
    'Variable': 'A storage location with a symbolic name in a program to hold data.',
    'Function': 'A block of organized, reusable code that performs a specific task.',
    'Conditional Statement': 'A statement that performs different actions based on whether a condition is true or false.',
    'Loop': 'A control flow statement for executing a block of code repeatedly.',
    'List': 'A data structure that stores an ordered collection of items.'
}

# Print the glossary entries with nicely formatted output and comments
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")  # Print the word and its meaning, with a newline for separation.

# Output will look like this:
# Variable:
# A storage location with a symbolic name in a program to hold data.
# 
# Function:
# A block of organized, reusable code that performs a specific task.
# 
# Conditional Statement:
# A statement that performs different actions based on whether a condition is true or false.
# 
# Loop:
# A control flow statement for executing a block of code repeatedly.
# 
# List:
# A data structure that stores an ordered collection of items.
