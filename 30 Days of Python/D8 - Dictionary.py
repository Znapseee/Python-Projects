student = {
    'first_name': 'John Mario',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': '23',
    'marital_status': 'Single',
    'skills': ['Programming', 'Simulation', 'Networking', 'Mathematics'],
    'country': 'Philippines',
    'city': 'Valenzuela City',
    'address': 'Secret'

}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type
print(type(student['skills']))

# Modify the skills values by adding one or two skills
print(student['skills'].extend(['Electronics', 'Cloud Computing']))

# Get the dictionary keys and values as list
print(student.keys())
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
print(student.pop('marital_status'))
print(student)

# Delete one of the dictionaries
del student