# Dictionaries
# Create and use dictionaries
# Dictionary methods and operators

"""
Doctionaries are collections of key value pairs
-unorderred
-mutable and 
-indexed by keys

"""

# Example 1: Create a dictionary

# Create a dictionary for a student persuing software engineering
# the keys must be name, age, technoloy interest, course and year of study

student_dictionary = {
    'name':'Ndjekornom Victoire',
    'age':23,
    'technology':'ML & Software development',
    'course':'BSSE',
    'year':'Year 2'
}

print(student_dictionary['name'])

# Access values 

# Modify values

# Exercice 1 

# Modify age and technology

student_dictionary['age'] = 34
student_dictionary['technology'] = 'Ai'

# Example 2 : Add email

student_dictionary['email'] = 'vndjekornom@gmail.com'


# Exercise 2 : Remove a key value pair from dictionary 

del student_dictionary['year']
# print(student_dictionary)

# Common dictionary methods

"""

get() //returns the value for the specified key if the key is in the dictionary
if not returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and returns the corresponding value

"""

# Example 3: Use the get() method  

print(student_dictionary.get('technology'))

physic = {
    'height': 167,
    'weight': 76
}


# Exercise 3 : update tyhe value of age 

student_dictionary.update(physic)
# print(student_dictionary)

# Exercice: Use if to check if key 'age' is in dictionary

if 'age' in student_dictionary.keys():
    print("Age:" ,student_dictionary['age'])


# keys(), values(), items() methods

"""
keys()  returrns a list containing all keys in the dictionary
value() returns a list containing all values in the dictionary
items() returns a list a tuple for each key value pairs 
"""
# Exercise 4 : Use update to change the age value and add a new key whatsapp to dict

update_values = {
    'course': 'CS',
    'whatsapp': '0706080193'
}

student_dictionary.update(update_values)

print(student_dictionary['course'],student_dictionary['whatsapp'])