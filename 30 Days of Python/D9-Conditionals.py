person = {
    'first_name' : 'Carl',
    'last_name' : 'Johnson',
    'age' : 250,
    'country' : 'Finland',
    'is_marred' : True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][len(person['skills']) // 2])


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print('Python')
else:
    print('None')

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# If the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# If the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if person['skills'] == ['JavaScript', 'React']:
    print('He is a front end developer')

elif person['skills'] == ['Node', 'Python', 'MongoDB']:
    print('He is a backend developer')

elif person['skills'] == ['React', 'Node', 'MongoDB']:
    print('He is a fullstack developer')

else:
    print('unknown title')


# If the person is married and if he lives in Finland, print the information in the following format: Name Surname lives in Finland. He is married.
if person['country'] == 'Finland':
    if person['is_marred'] == True:
        marital_status = 'married'
    else:
        marital_status = 'single'
    print(f'{person['first_name']} {person['last_name']} lives in Finland. He is {marital_status}')
