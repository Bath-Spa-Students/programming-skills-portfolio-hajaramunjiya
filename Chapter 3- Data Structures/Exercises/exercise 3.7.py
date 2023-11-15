# List of places to visit
places_to_visit = ['Tokyo', 'Paris', 'New York', 'Sydney', 'Rio de Janeiro']

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Show that the list is still in its original order
print("Original order after sorted():", places_to_visit)

# Print the list in reverse alphabetical order using sorted()
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the list is still in its original order
print("Original order after reverse sorted():", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Use reverse() again to change the order back to the original
places_to_visit.reverse()
print("Original order after reverse():", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit
