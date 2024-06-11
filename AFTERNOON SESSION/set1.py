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

#Lists

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