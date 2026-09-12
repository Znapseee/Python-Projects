# Exercise: Level 1

# Declare an emmpty list
list1 = []

# Declare a list with more than 5 items
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Find the length of your list
print(len(list2))

# Get the first item, the middle item, and the last item of the list
print(list2[0:12:5])

# Declare a list called mixed_data_types
mixed_data_types = ['Kevin', 23, 179, 'Single', 'Philippines']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the first, middle, and last company
print(it_companies[0:7:3])

# Print the list after modifying one of the companies
it_companies[6] = 'AWS'
print(it_companies)

# Add an IT company to the list
it_companies.append('Salesforce')

# Add an IT companies in the mmiddle of the company list
it_companies.insert(4, 'SAP')

# Capitalize one of the companies except IBM
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string
it_companies = '#, '.join(it_companies)
print(it_companies)

# Check if a certain company exist in the it_companies list
print('IBM' in it_companies)

# Sort the list using sort() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)

#  Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[4:])
