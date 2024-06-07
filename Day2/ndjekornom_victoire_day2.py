#Conditional are used to execute a peice of code only if the condition is true

age = 23

if age > 18:
    print("You are an adult")
elif age > 65:
    print("You are a senior citizen")
else:
    print("You are a youth")

#Example
#Grading system
grade = 78
if grade >= 90 :
    print(" Excellent")
elif grade >= 80:
    print("Very good")
elif grade >= 70 :
    print("Good")
else :
    print("Not good")

#Exercise
# Discount based on age
age = 17
if age < 13 :
    print("You get a discount of 1000")
elif age == 13 or age<18 :
    print("You get a discount of 500")
elif age >= 18 or age <65: 
    print("Adult pay full price 2000")
else:
    print("Senior citizens pay full price 5000")


#For loop# example

cars = ['Tesla','Audi','BMW','Jeep', 'RR']
for car in cars:
    print(car)
count = 1

#While loop 
while count <= 10:
    print(count)
    count = count + 1


#Exercice 2
my_favorite_colors = ['black', 'grey','white']

for color in my_favorite_colors:
    print(color)

count = 5 
while count>0:
    print(count)
    count -=1



