# print("hahao")
# print("My name is Sagar Tamang")
# #this is my first python comment 
# #variables 
# mok ="Sagar"
# print(f"Hello {mok}")
# food ="masu vat"
# print(f"I love {food}")
# email="sagarmoktan2369@gmail.com"
# print(f"My email is {email}")
# #integers
# ag=23
# print(ag)
# print(f"You are {ag} years old.")
# stu=True
# if stu:
#   print("You are a student.")
# else:
#   print("You are not a student.")
# name=""
# age=35
# gpa=3.6
# std=True
# print(type(stu))
# print(type(gpa))
# print(type(name))
# print(age)
# print(type(age))
# age=str(age)
# print(name)
# print(type(age))
# age+="5"
# print(age)
# name=bool(name)mo
# print(name)
# sa=input("Enter your name:")
# print(f"hello {sa}")
# ag=int(input("How old are you?"))
# # ag=int(ag)
# ag+=1
# print(f"You are {ag} years old.")
#exercise to calculate area of rectang;e
# len=int(input("whats the length of the rectangle:"))
# bre=int(input("whats the breadth of the rectangle:"))
# are=len*bre
# print(f"The area of the rectangle is {are}cm²")

#shopping cart 
# item=input("What are you trying to buy?")
# price=int(input("whats the price of the item?"))
# qun=int(input("how many?"))
# tot=price*qun
# print(f"You have bought {qun} {item}.Thank You ")
# print(f"Your total is Rs.{tot}.")

#madlibs game
#word game where you create a story by filling in blanks
# adjective1=input("Enter an adjective(description):")
# noun=input("Enter a noun(peron,place,thing):")
# adjective2=input("Enter an adjective(description):")
# verb1=input("enter a verb ending with 'ing':")
# adjective3=input("Enter an adjective (description):")
# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun}.")
# print(f"{noun} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")
# fr=0
# fr=fr+1
# fr+=1
# fr-=1
# fr*=3
# fr/=3
# fr=int(fr)
# print(type(fr))
# fr=3
# fr**=2
# print(fr)
 
#nested loop
# num_1 = "3434-43434-2323-232"
# for nu1b1 in num_1:
#   # print(nu1b1, end=" ")
#   print(nu1b1)

# rows = int(input("Enter the number of rows:"))
# column = int(input("Enter the number of columns: "))
# sym = input("Enter the symbol you want to print: ")
# for x in range(rows):
#   for y in range(column):
#     print(sym, end="")
#   print()

 #collection = single "variable" used to multiple values
# list = [] ordered and changable. Duplicates OK
# set = {} unordered and immutable, but add/remoe ok. No duplicates
# tuple = () ordered and unchangeable. Duplicates Ok. Faster   

# fruits = ["mango","banana","orange", "pineapple"]
# print(fruits[::3]) #for jumping numbers
# print(fruits[0:3:2]) #range and jumping value at last 
# for fruit in fruits:
#   print(fruit, end= " & ")
# print(dir(fruits)) # lists different actions that can be performed on the paramater of dir
# print(help(fruits)) # shows all the things we can do to the parameter of help
# print("mango" in fruits)
# print("Kiwi" in fruits)
# fruits[0] = "Kiwi"
# print(fruits)
# fruits.append("mango")
# print(fruits)

# try:
#   fruits.remove("oragne")
#   print(fruits)
# except ValueError:
#   print("Sorry couldn't find the element in the list")
# finally:
#   frui = input("Please reenter the value you want to remove: ")
#   fruits.remove(frui)
# print(fruits.clear())
# print(fruits.count("apple"))

# cars = set()
# print(type(cars))
# cars = {"audi","mercides","labo","suzuki","audi"}
# # print(cars)
# # print(dir(cars))
# # print(help(cars))
# print("Koniseg" in cars)
# # print(cars[3]) 
# cars.add("koniseg")
# cars.remove("audi")
# cars.pop()
# print(cars)

# touples
# fruits = ("apple","mango","banana")
# print(fruits)
# print(fruits.index("apple"))
# print(fruits.count("mango"))

# foods = []
# prices = []
# total = 0
# price = 0
# foo = ""
# while True:
#   foo = input("Enter a food to buy(Q/q to quit): ")
#   if foo == "Q" or foo == "q":
#     break
#   else:
#     price = float(input(f"Enter the price of {foo}: Rs. "))
#     foods.append(foo)
#     prices.append(price)
#     total += price
# print("Your bill:")
# for food in foods:
#   print(food, end= " ")
# print()
# for price in prices:
#   print(price,end= " ")
# print(f"\nTotal= Rs.{total}")

# 2d list
# fruits = ("apple", "mango", "pineapple", "banana")
# vagetables = ("carrot", "celery", "potatoes")
# meats = ("chicken", "mutton", "fish")
# groceries = {fruits, vagetables, meats}
# for foods in groceries:
#   print(foods[0][2],end=" ")
#   print()
# print(groceries[0][2]) #for individual elements inside list elements
# i = 0
# while i < len(groceries):
#   print(groceries[i])
#   i += 1

# list_1 = [1,2,3]
# list_2 = [4,5,6]
# list_3 = [7,8,9]
# list_4 = ["*",0,"#"]
# fin_list = [list_1,list_2,list_3,list_4]
# print(fin_list,end= " ")
# print("Simple calculator form: ")
# for row in fin_list:
#   i = 0
#   print(row[i],row[i+1],row[i+2])
#   i += 1

#same as above but a little different 
# print("    Simple Calculator \n \n  ")
# for row in fin_list:
#   for nur in row:
#     print("    ",nur, end= " ")
#   print()


#quiz in python
# questions = ("How many elements are there in periodic table?: ",
#              "Which animal lays the largest eggs?: ",
#              "How many bones are there in the human body?: ",
#              "Which planet in the solar system is the hottest? ")
# options = (
#   ("A. 113","B. 118","C. 116","D. 117"),
#   ("A. Ostrich","B. Kiwi","C. Penguin","D. Golden Eagle"),
#   ("A. 200","B.210","C. 206 ","D. 300"),
#   ("A. Earth","B. Mars","C. Venus ","D. Jupiter"))
# answers = ("C","A","C","C")
# score = 0
# i = 1
# qstn_num = 0
# for queston in questions:
#   print(f"\n{i}. {queston}")
#   for option in options[qstn_num]:
#     print(option, end= " ")
#     print()
#   ans = input("Enter the answer: ").upper()
#   i += 1
#   if ans == answers[qstn_num]:
#     score += 1
#   qstn_num += 1
# print("You scored: ",score," in the test.")

