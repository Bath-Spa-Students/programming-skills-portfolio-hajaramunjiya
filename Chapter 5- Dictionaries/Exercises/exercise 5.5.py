# Create dictionaries for different pets with information about the kind of animal and owner's name.
pet1 = {
    'animal_kind': 'Dog',
    'owner_name': 'naja'
}

pet2 = {
    'animal_kind': 'hamster',
    'owner_name': 'aisha'
}

pet3 = {
    'animal_kind': 'Parrot',
    'owner_name': 'azraa'
}

# Store these pet dictionaries in a list called 'pets'.
pets = [pet1, pet2, pet3]

# Loop through the list of pets and print information about each pet.
print("Information about Different Pets:")

for pet in pets:
    print("\nPet Information:")
    print(f"Animal Kind: {pet['animal_kind']}")
    print(f"Owner's Name: {pet['owner_name']}")

#We use a loop to iterate through the list and print information about each pet, including their animal kind and owner's name.