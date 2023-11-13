#Use a dictionary to store information about yourself
# Create a dictionary to store information about yourself
personal_info = {
    'name': 'hajara',
    'age': 19,
    'gender': 'Female',
    'location': 'City, Country',
    'occupation': 'student',
    'hobbies': ['Reading', 'Coding', 'spending time alone'],
    'contact_info': {
        'email': 'your.email@example.com',
        'phone': '+1234567890'
    }
}
#the personal_info dictionary stores various details about yourself, including name, age, gender, location, occupation, hobbies, and contact information.

# Display information about yourself
print("Personal Information:")
print(f"Name: {personal_info['name']}")
print(f"Age: {personal_info['age']}")
print(f"Gender: {personal_info['gender']}")
print(f"Location: {personal_info['location']}")
print(f"Occupation: {personal_info['occupation']}")
print(f"Hobbies: {', '.join(personal_info['hobbies'])}")
#the personal_info dictionary stores various details about yourself, including name, age, gender, location, occupation, hobbies, and contact information.

# Display contact information
print("\nContact Information:")
print(f"Email: {personal_info['contact_info']['email']}")
print(f"Phone: {personal_info['contact_info']['phone']}")
