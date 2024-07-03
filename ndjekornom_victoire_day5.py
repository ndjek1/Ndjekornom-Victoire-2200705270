# Defining functions 

# Function syntax, parameters
# Return value
# lambda function

# Functions in python are defined using the 'def' keyword, followed by function name 
# parenthesises (), and inside the parenthesises we pass the parameter name and the colon

# Example 1: 

def multiply(a,b):
    return a*b 

product = multiply(4,6)
print(product)

# # Example 2: multiple return values

def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print("x:",x,"y:",y)


# Exercise 1: Define a function greet with a parameter name, set to "gest" and print a message 
# i am a software programmer

def greet(name = "Victoire"):

    return f"I am {name}.", "And i am a software programmer"
    
name, position = greet()
print(name,position)

# Exercise 4 : Return multiple values of name and age
def get_name_and_age():
    name = "Victoire"
    age = 43
    return name, age
name, age = get_name_and_age()

print("Name is:",name,"and i am",age,"years old")

# Notes 
"""_summary_

def: key word that tells python the we are dealing with a function
function_name: Nmae of the function
parameters: Optional, arguments (values) passed to the function
Docstrings: Optional, describes the function purpose
return: Optional, returns a value from a function
"""

# Function definition syntax

def function_name(parameters):
    """Docstring optional"""
    # function value
    return #values

# Lambda function
# They are small anonymous functions defined using the 'lambda' keyword 
# They are syntactically restricted to single expression

# syntax for lambda function

# lambda parameter : expression 

add = lambda a, b :a + b
print(add(4,3))

# Use lambda to sort

coordinates = ((3.1),(1,5),(4,6),(0,4),(1,0))

sorted_coordinates = sorted(coordinates, key=lambda coord: coord[0])
print(sorted_coordinates)

# Map, filter and reduce

# Example 6: 

number_squares = [1,2,3,4,5]

squared_numbers = list(map(lambda x: x**2, number_squares))

print(squared_numbers)

#  Define a function to get user info that accept arbitrary keyword arguments and print the key value pair

def get_user_input(**args):
    for key, value in args.items():
        print(key,value)


get_user_input(age=23,name='Victoire',position='software dev')





