#Write a Python program to iterate through both the keys and values of a dictionary and print them

# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Iterate through keys and values and print them
# we use the items() method to iterate through both keys and values simultaneously
print("Keys and values of the dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
    #The for loop unpacks each pair into key and value, which are then printed.
