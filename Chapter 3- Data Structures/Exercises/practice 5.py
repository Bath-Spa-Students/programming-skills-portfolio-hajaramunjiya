#You have given a Python list. Write a program to find value 20 in the list, and if it is present,replace it with 200. Only update the first occurrence of an item.Work with the given list:
#list1 = [5, 10, 15, 20, 25, 50, 20]

#we iterate through the list1 using a for loop and check for the first occurrence of 20
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find the first occurrence of 20 and replace it with 200
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break  # Break the loop after the first occurrence is updated
#When we find it, we replace it with 200 and then use break to exit the loop.

# Print the updated list
print(list1)
#fter running this code, the first occurrence of 20 will be replaced with 200 in the list