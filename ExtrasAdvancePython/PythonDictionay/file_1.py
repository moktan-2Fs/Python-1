empty_dict = {
    "name": "Moktan",
    'age': 23,
    "college": "Kist"
}
# print(empty_dict)
# print(type(empty_dict))
for key, value in empty_dict.items():
    print(f"{key} = {value}",end="\n")
# dictionary length
print("The length of the dictionary is:",len(empty_dict))

# key names in the items using the names of the keys
print(empty_dict["name"])
print(empty_dict["age"])
print(empty_dict["college"])

# get() method gets element, if there is no such element then returns the None value
print()
print(empty_dict.get("age"))
print(empty_dict.get("City"))

# adding to a dictionary using key names 
empty_dict["Province"] = "Bagmati"
empty_dict['Ward No.'] = 32
print(empty_dict)

#modifying items in a dictionary 
empty_dict["name"] = "Sagar"
empty_dict["college"] = "V.s Niketan"
print(empty_dict)

# checking keys in a dictionary using "in" which returns boolean value 
print("name" in empty_dict)
a = "Cast" in empty_dict
print(a)

# copying a dictionary
copied_dict = empty_dict.copy()
print("This is the print of the copied dicitonary..",copied_dict)

# deleting or removing key:values from a dictionary 
# pop(key), removes the item with specified key name
# popitem(), removes the last item from the dictionary
# del dict[key], removes item with specified key 
print(empty_dict.pop("age"))
print(empty_dict)
empty_dict.popitem()
print(empty_dict)
del empty_dict["name"]
# del empty_dict deletes the whole dictionary 
print(empty_dict)
print(empty_dict)
for dic in empty_dict.items():
    print(dic)

# getting dictionary keys as a list
keys1 = copied_dict.keys()
print(keys1)

# getting dictionary values as a list
valuess = copied_dict.values()
print(valuess)

# clearing a dictionary 
copied_dict.clear()
print(copied_dict)