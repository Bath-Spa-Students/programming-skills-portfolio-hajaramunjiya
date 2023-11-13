#Write a Python program to merge two dictionaries into one

# Sample dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

# Merge dictionaries
merged_dict = {**dict1, **dict2}
#the {**dict1, **dict2} syntax is used to merge the dictionaries

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)
#If there are common keys, the values from the second dictionary (dict2 in this case) will overwrite the values from the first dictionary (dict1).