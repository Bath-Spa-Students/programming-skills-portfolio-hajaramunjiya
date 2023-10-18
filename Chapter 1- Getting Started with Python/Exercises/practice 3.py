# You need to make a program for al leaderboard. The program needs to output the numbers 1 to 9, each on a separate line followed by a dot

def print_leaderboard():
    # Iterate from 1 to 9
    for i in range(1, 10):
        # Print the number
        print(i, end="")  # Print the number without a newline
        print(".", end="\n")  # Print a dot and move to the next line

# Call the function to print the leaderboard
print_leaderboard()

#We define a function print_leaderboard() to print the leaderboard.
#Inside the function, we use a for loop to iterate from 1 to 9.
#In each iteration, we use print(i, end="") to print the number without a newline.
#We then use print(".", end="\n") to print a dot and move to the next line.