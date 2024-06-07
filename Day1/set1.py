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