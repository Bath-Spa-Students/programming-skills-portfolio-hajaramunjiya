#Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100

# Initialize a variable to store the sum
total_sum = 0
#total_sum is initialized to zero, and then a for loop is used to iterate through the numbers from 1 to 100

# Use a for loop to iterate through numbers from 1 to 100
for number in range(1, 101):
    total_sum += number
    #The total_sum is updated in each iteration to accumulate the sum

# Print the sum
print("The sum of numbers from 1 to 100 is:", total_sum)
