
#Lists
# Exercise 1
#1 Create list
my_list = ["black", "grey", "white", "navi", "dark blue"]
#output 2nd element
print(my_list[1])

#2 Change the value opf the first iitem to a new value
my_list[0] = "maroon"

#3 add a sixth item to the list

list.append("dark green")

#4 Add "Bathel" as the item 
my_list.insert(2,"Bathel")

#5 Remove the 4th item from the list 

del my_list[3]

#6 Use the negative index to print last item in list
print(my_list[-1])

#7 Create new list with 7 items and use range to print items

list2 = ["a","b","c","d","e","f","g"]
print(list2[2:5])

#8 Create a list of countries

countries = ["Chad", "Uganda", "Rwanda", "Kenya", "Cameroon"]
copy_list = countries.copy()

#9 Loop through list of countries

for country in countries:
    print("The country is :", country)

#10  List of animal names and sort in assending and descending order

animals = list(('Cat', "snake", 'Rakoon', "Anaconda",'python'))
animals.sort() # Assinding order
animals.sort(reverse=True) # Descending order

# Output animals with 'a' in only

for x in animals:
    if 'a' in x:
        print(x)

#12  A list containing first names and second names then join them

first_names = ["Ndjekornom", "Cyiza Ndoli" ,"Mulindwa", "Assimire","Efrata"]
last_names = ["Victoire", "Jean de Dieu" ,"Yusuf", "Patricia","Aaron"]

full_names = first_names.extend(last_names)

# Tuples
# Exercise 2 

# 1 Write a python code to output the favorite phone brand from the tuple

x = ("sumsung", "iphone","tecno", "redmi")
print(x[0])

# 2 Using negative index to print 2nd last item 

print(x[-2])

# 3 Replace iphone with itel in the list above
y = list(x)
y[1] = "itel"
x = tuple(y) 
print(x[1])

# 4 Write python code to add Huawei to the tuple 

y = list(x)
y.append("Huawei")
x= tuple(y)


# 5 Writing python code to loop through the tuple
print("\nFoor loop")
for item in x :
    print(item)

print("\nWhile loop")
i = 0
while i<len(x):
    print(x[i])
    i+=1

# 6 Python code to remove or delete the first item in the tuple

y = list(x)
y.pop(0)
x= tuple(y)
print(x)

#  7 Using the tuple() constructor create a list of cities in uganda

cities = tuple(("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"))

# 8 Unpack the tuple

(Central, West, *East) = cities

print(Central)
print(West)
print(East)

# 9 Use range to print 2nd, 3rd, 4th cities in the tuple

print(cities[1:4])

# 10 Joining tuples  

first_names = ("Ndjekornom", "Cyiza Ndoli" ,"Mulindwa", "Assimire","Efrata")
last_names = ("Victoire", "Jean de Dieu" ,"Yusuf", "Patricia","Aaron")

full_names = first_names + last_names

# 11 Multiply a tuple of colors by 3

colors = tuple(("Black", "Grey", "White"))

my_tuple = colors*3

print(my_tuple)

# 12 return the number of times 8  appears in thistuple = (1,3,7,8,7,5,4,6,8,5)

thistuple = (1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))



# Sets  
# Exercise 3
# 1 Use set() constructor to create a set of 3 beverages

my_beverages = set(("Miranda", "Pepsi", "Novida"))

# 2 Use the correct method to add two more beverages to the set

my_beverages.add("Juice")

# 3   Check if item is pressent in set

mySet = {"Oven", "kettle", "microwave","refrigerator"}

print("microwave" in mySet)

# 4 remove kettle from set

mySet.remove("kettle")  #or 
mySet.discard("kettle")

# 5 Loop through the set 

for x in mySet:
    print(x)

# 6 Add items from a list to a set

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

# 7 Joining set 

first_names = {"Ndjekornom", "Cyiza Ndoli" ,"Mulindwa", "Assimire","Efrata"}
ages = {23,23,22,21,20}

final_set = first_names | ages  #or 
final_set= first_names.union(ages)

# Strings 
# Exercise 4
# 1 Concatenating an integer and a string

number = 1
name = "Jeff"

concatenated = f"{name} has {number} cars"
print(concatenated)

# 2 Remove extra space in string

txt = "     Hello,    Uganda!   "

cleaned_text = ' '.join(txt.split())

print(cleaned_text)

# 3 Covert values yo uppercase

txtUpper = cleaned_text.upper()
print(txtUpper)

# 4 replace 'U' with 'V' in txt

print(txt.replace("U","V"))

# 5 Return a range of characters from a string

y = "I am proudly a chadian!"

print(y[1:5])

# Depug the code

# x = "All "Data Scientists" are cool "

x = "All 'Data scientists' are cool"


# Dictionaries 
# Exercise 5
Shoes = {
    "brand":"Nick",
    "color":"black",
    "size": 40,
}
#1 print the value of the shoe size 
print(Shoes["size"])

#2 change the value of "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

print(Shoes["brand"])

#3 Adding a key/value pair "type":"sneakers"

Shoes["type"] = "sneakers"

print(Shoes["type"])

#4 Return the list of all the keys in the dictionary

keysList = Shoes.keys()
print(list(keysList))


#5 Return the list of all the values in the dictionary
values = Shoes.values()
print(list(values))

#6 check if size exist in dictionary

if Shoes["size"]:
    print("Key size exist")

#7 Loop through a dictionary

for x in Shoes: # prints the keys only
    print(x)

for x in Shoes.values(): # returns only the values
    print(x)

for x in Shoes.keys(): # Returns the keys only
    print(x)

for key, value in Shoes.items():
    print(key, ":", value)


#8 Remove color from the dictionary

Shoes.pop("color")

print(Shoes.keys())

#9 Empty the dictionary

Shoes.clear()
print(list(Shoes.keys()))

#10 Make a copy of a dictionary

Original = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

CopyDict = Original.copy()

print(CopyDict)

#11 Nested dictionaries   


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Each key in the parent dictionary has a dictionary with key/value pairs as value






