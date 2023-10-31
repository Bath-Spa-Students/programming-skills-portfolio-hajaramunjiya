# Define a dictionary with river names as keys and their respective countries as values.
rivers = {
    'mississippi': 'united states',
    'fraser': 'canada',
    'River Severn': 'UK',
}

# Loop through the dictionary to print a sentence about each river and its associated country.
for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

# Print a section header and list all the rivers included in the dataset.
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

# Print another section header and list all the countries included in the dataset.
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
