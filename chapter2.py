# variables = containers that is used to store something and use it using the variable name
# b = 2
# a = b             
# print(a + b)      
# name = "haarry"

# primary data types in python
#  a = 1integers 
#  b = 3.34floothing point num
#  name = "moktan" strings
#  boll = True Boolean
#  e = None None type

# _one = 1
# one1 = 2
# one@21 = 3 # invalid because of @ 
# print(one1)

#operators
# b = 2
# b += 4  #increment the value of b by 4 and assign to b
# print(b)
# if 4==1:
#  print("its true")
# else:
#  print("its false")
#comparison operators always return boolen value
# d = 5 > 6
# print(d)
 
# #logical operators its like OR and AND logic table
# e = False and False # alt + select line is used for multi line insersion
# print(e)
# print(not(False)) #not make the inverse of the boolean it is used on

# a = "sagar" #string
# b = 3 #integer
# d = "34.53" #string anything inside " " is a string 
# c = 3.34 #float
# print(type(d))

# a = bool(input("Enter number 1: ")) here instead of bool other datatypes can be used accordingly
# b = bool(input("Enter number 2: ")) # alt + shift + down arrow for replicating a line
# print("Number 1 is: ", a)
# print("Number 1 is: ", b)
# print("Sum is : ", a + b)

#prictice set 
#q1,q3,q4 
# a = float(input("Enter any number: "))
# b = int(input("Enter 2nd number: "))
# print(f"The square of {b} is {b**2}.")
# print(f"The average of the two numbers is {int((a+b)/2)}.")
# print(type(a))
# print(type(b))
# print(a>b)
# print(a<b)
# print(a==b)
# print(a>=b)
# print("The sum is:", int(a + b))

#q2
# c = a % 2
# print("The remainder is:", type(c), int(c))

#strings "",'',''' ''' are used for making string in python
# name = "sagar"
# nam1 = 'sagar'
# name2 = '''thi s
# sflsj s
# fsfjslf '''

# string1 = "Moktna" 
# print(string1[4])
# print(string1[0:3]) #means start from index 0 and print till 3rd index
# char1 = string1[4] #assigns the value of 4 index of string1 to char1
# print(char1)
# print(string1[:4])
# print(string1[3:])

# #skip value
# a = "abcdefghijklmnopqrstuvwxyz"
# print(a[2:24:3]) # gives cfilorux to understand take between 2to 24 and 
# print(a[24])     # give the value of 2 and jump 3 steps and give its value and repeat it until 24
  
#python is a case sensitive language

 #funcions of string
# strn = "sagar moktan is a don"
# print(len(strn))
# print(strn.endswith("or")) #false 
# print(strn.endswith("ar")) #true
# print(strn.startswith("ma")) #false
# print(strn.startswith("sa")) #true
# print(strn.capitalize()) #capatalizes the stating character of the string only
# print(strn.replace("moktan","Tamang")) # not for the original string but temporarily for this line only
# print(strn) #here its as the original string 

# escape sequence characters
# ex: \n(new line),\t(tab),\;(singlequote,\\(backslash))
# a = "sagar is a ver\t good person \n " \
# "this is also  a very \" valid reason \" to trust\ sagar\n" \
# "but its not always true"
# print(a)
 
#practice 3
#q1
# inp = input("Enter your name: ")
# print(f" Good afternoon Mr. {inp}")
# #2
# name = input("Enter your name: ")
# date_fin = "2082/09/24"
# print(f"""
#           Dear {name},
#           You are selected!
#           {date_fin}
# """)
# replace 
# twwk = """
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star."""
# print(twwk.replace("twinkle","winkle").replace("Twinkle","Winkle")) #chaining in replace 

# name = "sagar tamang  is a very good person"
# print(name.find("  ")) #to find any thing inside the sting and return its address
# print(name.replace("  "," "))#if not found the it returns -1 
# strings are immutable which means u cannot change them by runnin functions on them

#q4
# letter = "Dear Harry, \nthis python course is nice. \nThanks"
# print(letter)

#chapter 4

#list unlike strings lists are mutable and its values are changeable
# friends = ["Sagar","Subash","orange",5, 555.3,"mango",False]
# print(friends[-1])
# print(friends[3])
# friends[1] = "moktan" #list can be indexed
# print(friends[1])
# print(friends[1:5:2]) #every thing like slicing and skipping can be done to list
#  # in list changing somthing changes in itself unlike string where new string is formed 
#  # when changing something 
# print(friends)
# friends.append("shani") #.append adds at last
# print(friends)
# f1 = [1,3,333,343,3,335,334,343,6]
# f1.sort()
# f1.reverse()
# print(f1)
# f1.insert(3,44) #insert 44 such that its index in list is 3
# print(f1)
# print(f1.pop(6))
# print(f1.pop(6))
# f1.insert(6,0)
# print(f1)
# print(f1.sort()) #in string this would work but gives none in list 
# # because read 164 165
# f1.remove(335)
# print(f1)

#dictationary 
# marks = {
#     "sagar": 300,
#     "ishaque": 500,
#     "sakshyam": 333,
#     "ishaque": 332,
#     "rohan": "kumar",
#     "list1": [5,3,2,"moktan","Roshan"]
# }

# # list_list = [["moktan",500,20],[1,2,3,"og"], [55,44,66,"gamvhira"]] #list of list
# # print(list_list)
# # print(list_list[0])
# # print(list_list[2][3])

# print(marks, type(marks))
# print(marks["ishaque"])
# print(marks["sagar"])
# print(marks["rohan"])
# print(marks["sakshyam"])
# print(marks["list1"][3]) # accessing elements of list in a dictationary 

# marks = {
#     "sagar": 300,
#     "ishaque": 500,
#     "sakshyam": 333,
#     "ishaque": 332,
#     "rohan": "kumar",
#     "list1": [5,3,2,"moktan","Roshan"],
#     0: "oalala", 
# }
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"rohan":100, "sujan": 645, 5: "mohan ", "list1":["komal"]})
# print(marks)
# print(marks.get("list1"))
# marks["list1"].append("new_item") # adding new elements to list inside dictationary
# marks["list1"][3] = "Tamang"  #changing individual elements inside list inside dictationay 
# marks["list1"].remove("Roshan") #removing elements from list
# marks["list1"].insert(2, 10000)  #inserting in a specified locatiion 
# marks["list1"].insert(1, "lalallalala")
# print(marks["list1"][1])

# https://youtu.be/m8oVwoGy6L8

#sets = only takes every values only once and doesnt repeat it 
# dic_empt = {

# }
# sets_1 = {1,3,4,3,5,6,7,7,"moktan"} #initing set 
# e = set() # creating empty set 
# print(sets_1) 
# e.add(5) #adding set members 
# e.add("mohan")
# # e.clear()
# print(len(e)) #length 
# sets_1.remove(5)
# sets_1.remove(7)
# print(e, type(e))
# a = sets_1.pop()
# b = sets_1.pop()
# c = sets_1.pop()
# print(a, b, c)
# print(sets_1) 

#union in set 
# s1 = {3,5,7,2}
# s2 = {2,6,8,5}
# print(s1.union(s2)) #takes one set as argument 
# print(s1.intersection(s2))

# names problem 
dict_1 = {}
i = 0
while i<=2:
    a = input("Enter your name: ")
    b= input("Enter your favourite language: ")
    dict_1.update({a:b})
    i += 1
print(dict_1)