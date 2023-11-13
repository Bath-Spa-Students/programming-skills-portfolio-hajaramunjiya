#Write a Python program that uses the elif statement to determine the season based on the month provided as input.

# Get the month as input
month = input("Enter the month: ")

# Convert the input to lowercase for case-insensitivity
month = month.lower()

#the program takes the month as input, converts it to lowercase for case-insensitivity, and then uses the elif statement
# Check the season based on the month
if month in ['december', 'january', 'february']:
    season = "Winter"
elif month in ['march', 'april', 'may']:
    season = "Spring"
elif month in ['june', 'july', 'august']:
    season = "Summer"
elif month in ['september', 'october', 'november']:
    season = "Autumn"
else:
    season = "Invalid month"

# Display the result
print(f"The season for {month} is {season}")

