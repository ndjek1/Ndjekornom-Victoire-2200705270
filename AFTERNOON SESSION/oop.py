
class Person:
    
    #constructor
    #Whenever we use the class to crate an object the constructor will be called.
    def __init__(self,name, age, isSick):
        self.name = name
        self.age = age
        self.isSick = isSick
    
    #__str__ method is used to specify how the obeject is represented when we make a string
    def __str__(self):
        return f"{self.name}({self.age})"

#We also know that a persron does things and they are called methods
    def present_self(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old")

    

#Creating an object 
person = Person("Jane", 24, False)

#We can access the attributes or properties of a person using the following syntax

name, age = person.name, person.age  #Which will return the name of that particular person

print(name,age)
