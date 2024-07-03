#  Inheritance and polymorphism

"""
Inheritance and method overriding

Polymorphism and method resolution order
Abstract classes and interfaces
"""

# Inheritance and method overriding
"""
Inheritance and method overriding allows a class(child) to inherit attributes and methods
from another class (parent class)

Key concepts
Base class (parent class):Class whose properties inherited  by another class.
Derived class (child class): Class that inherits attributes and methods from another base class

"""

# Example 1: Cresate a class where a dog inherits from animal and overrides with a speak method

class Animal:
    def speak(self):
        return "Make a sound"
    

class Dog(Animal):
    def speak(self):
        return "Barks"
    

# implementation of inheritance

animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())     


# Polymorphism and method resolution
# Polymorphism allows objects of different classes to be traited as objects of a common superclass
# Method resolution order is order in which python looks for a method in a hierarchy classes

# Example 2: How polymorphism works

class Animal:
    def speak(self):
        return "Make a sound"
    

class Dog(Animal):

    def speak(self):
        return "Barks"
    

class Cat(Animal):

    def speak(self):
        return "Meoww"
    
def make_animal_speak(animal):
    print(animal.speak())


animal = Animal()
dog = Dog()
cat = Cat()


# Exercise 1:
# Create a simple application to manage different types of vihecules
# Implement derived class to demonstrate inheritance and polymorphism
"""
Requirements
1. Base classs to vehecule
Attributes: Make, model and year
Methods: display_info()

2. Derived class 
Car: inherits from vehicle
attributes: number_of_doors
Overrides: display info

Motorcycle: inherits vehicle
attributes: type(cruiser,sport,touring)

"""

class Vehicle():

    def __init__(self,make,model,year) :
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
    

class Car(Vehicle):

    def __init__(self, make, model, year,number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return f"Number of doors: {self.number_of_doors}"
    

class Motorcycle(Vehicle):

    def __init__(self, make, model, year,type_of):
        super().__init__(make, model, year)
        self.type_of = type_of

    def display_info(self):
        return f"Type of motorcycle is: {self.type_of}"
    

        
# Exercise 2: Create a function that accepts a list of vehicle objects and call thei display_info() method
# to print details of each vehicle

def print_list_of_vehicles(listOfVehicles):

    for vehicle in listOfVehicles:
        print(vehicle.display_info())


vehicles = [Vehicle("Toyota","Jaguar","2018"),Car("Toyota","Ford","2020",4),Motorcycle("Honda","M60","2012","sport")]

print_list_of_vehicles(vehicles)


# Reading and writing files in python
"""
1. Working with text files

Handling CSV files 
JSON and XML file processing
"""
# 1 Working with files, open, read, write and close
# Note: Python provides inbuilt functions to handle text files

# Key concepts

"""
Opening file: open() function(r,w,a,r+)
Reading file: read() function
Writing file: write() function
Closing file: close() function   
"""


# Example 3: Write a file and read a file

# wriring in a text file
with open("victoire.txt",'w') as file:
    file.write('I am Ndjekornom Victoire and i am a big fun of robotics\n')
    file.write('I want to use python on robotics')


# Reading from a text file
with open("victoire.txt",'r') as file:
    content = file.read()
    print(content)


# Handling CSV files

"""
CSV (Comma Separeted Values) files
Widely used for data exchange

Key concepts: 
Reading CSV files: Using 'csv.reader()'
Writing CSV files: Using 'csv.writer()'
DictReader and DictWriter: The class read and write CSV files as dictionaries


"""

# Example 4: Writing and Reading CSV files

import csv

# Writing to a csv file

with open("victoire.csv", 'w',newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['name', 'position','course'])
    writer.writerow(['Ndjekornom Victoire','Student','BSSE'])
    writer.writerow(['Someone else','Trainee','Company'])


# Read from a csv file
with open("victoire.csv", 'r',newline='') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)
# # JSON and XML file processing

"""
JSON (Javascript object notation) and XML (Extensible Markup Language)
are formats used to structure data

Key concepts 
Loading json data: using json.load() for reading a json file
Dumping JSON data: using json.dump() forwriting JSON data
Passing JSON data: using json.loads() to handle JSON strings


"""

import json
# Writing to a JSON file

student_data = {
    'name' : "Victoire",
    'course' : 'BSSE',
    'year' : 'year 3'
}

with open('student_data.json',  'w') as json_file:
    json.dump(student_data, json_file)


# # Reading the JSON file

with open('student_data.json','r') as json_file:
    student_data1 = json.load(json_file)

    print(student_data1)


# Exercise 2: Write and read xml files
import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("Students_records")

# Create a child element
student1 = ET.SubElement(root, 'student')
student1.set('id', "1")
name1 = ET.SubElement(student1,"name")
name1.text = "Ndjekornom Victoire"
course1 = ET.SubElement(student1,"course")
course1.text = "BSSE"

# Create another child element
student2 = ET.SubElement(root, 'student')
student2.set('id', "2")
name2 = ET.SubElement(student2,"name")
name2.text = "Some other student"
course2 = ET.SubElement(student2,"course")
course2.text = "CS"

# Create the tree and write to a file

tree = ET.ElementTree(root)
tree.write("student.xml", encoding='utf-8', xml_declaration=True)

# Reading from xml file 

import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("student.xml")
root = tree.getroot()

# Iterate through each each
for student in root.findall('student'):
    student_id = student.get('id')
    name = student.find('name').text
    course = student.find('course').text
    print(f"Student ID: {student_id}")
    print(f"Title: {name}")
    print(f"Author: {course}")
    print("-" * 20)



# Ecercise 3: Using abstraction calculate the area and perimeter of a rectangle

from abc import ABC, abstractmethod

class shape(ABC):

    # abstractmethod is a decorator used to make a method abstract that makes the class abstract
    @abstractmethod
    def calculate_area(self,length, width):
        pass
    @abstractmethod
    def calculate_perimeter(self, length, width):
        pass

# We cannot create objects of the class shape because it has abstract methods
# When another class extends it it should give a method definition to the abstract methods 
# Otherwise it becomes abstract itself

class Rectangle(shape):

    def calculate_area(self, length, width):
        return length*width
    
    def calculate_perimeter(self, length, width):
        return (length+width)*2
    
rectangle = Rectangle()

area = rectangle.calculate_area(4,6)
print(area)
perimeter = rectangle.calculate_perimeter(4,6)
print(perimeter)

# https://github.com/ndjek1/Python.git