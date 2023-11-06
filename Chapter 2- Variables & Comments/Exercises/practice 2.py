# Initialize a variable to store the total marks
total_marks = 500

# Initialize a variable to store the sum of course marks
total_course_marks = 0

# Prompt the user for the number of courses
num_courses = int(input("Enter the number of courses: "))

# Iterate through the courses and collect their marks
for i in range(num_courses):
    course_marks = float(input(f"Enter the marks for course {i + 1}: "))
    total_course_marks += course_marks

# Calculate the average of course marks
average_marks = total_course_marks / num_courses

# Calculate the student's percentage
percentage = (total_course_marks / total_marks) * 100

# Print the average marks and percentage
print(f"Average marks for {num_courses} courses: {average_marks:.2f}")
print(f"Student's percentage: {percentage:.2f}%")
