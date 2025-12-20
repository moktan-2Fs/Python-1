# def to define a function
# def calc_sum(a,b): return a+b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(calc_sum(num1,num2))
# print(calc_sum(5,8)+calc_sum(num1,num2))

# def cal_ave(a=1,b=1,c=1):
#   return (a+b+c)/3
# print(cal_ave(5,3))

# def hello():
#   print("hello moktan")
# for i in range(8):
#   hello()

# def mul_2(a=1,b=1):
#     return a*b
# print(mul_2())

# list_1 = ["sagar","kamala","dolakha",6,5,33,3]
# def len_gi(a):
#     for i in a:
#         print(i,end = " ")
#     return len(a)
# len_gi(list_1)

# def factorl(n):
#   fact = 1
#   for i in range(1,n+1):
#     fact *= i
#   print(fact)
# f = int(input("enter the number whichs factorial you want: "))
# factorl(f)

# currency conversion
# rate = 143.5
# neprs = 0
# def convers(a):
#     a /= rate
#     return a
# neprs = int(input("Enter the amount you want to convert: "))
# usd = convers(neprs)
# print(f"Rs.{neprs} = {usd:.2f}$")

# recursion
# def show(n):
#     if n == 0: # this is a base case for recursion that
#         return  # stops the recursion and returns the values
#     print(n)
#     show(n-1)
#     print("prints while returning from basecase")
# show(5)

# call stack for understanding recursion
# def re_fact(n):
#     if n == 0 or n == 1 :
#         return 1
#     return n*re_fact(n-1)

# f = open("ignofile.txt", "r")

# # reads the first line from the file(only 1st line and rest can be also done in line or as a whole by read())
# data_infile_line1 = f.readline()
# # sending parameters gives the characters in the parameters numbers eg: (5) gives first 5 characters from the file
# data_infile = f.read()
# print(data_infile_line1)
# print(type(data_infile))
# print(data_infile, end="")
# f.close()

# "r" for reading
# "w" for writing
# "x" for new file and open for writing
# "a" for appending to the end of the file if it exists
# "b" binary mode
# "t" text mode(default)
# "+" open a disk file for updationg (reading and writing )

# writing to a file
# f = open("ignofile.txt", "a")
# f.write('Also I love girls with certain behaviours... \n')
# print(f)
# f.close()

# f = open("ignofile.txt", "r")
# print(f.read())
# f.close()
# prifi = None
# my_list = ["Sagar", "Moktan", "Tamang", "is", "a", "Don."]
# with open("ignofile.txt", "r") as file:



    # for fi in my_list:
    #     file.write(fi)
    #     print("\n")
    # prifi = file.read()
    #  print(prifi)
    #  for word in prifi:
    #      print(word, end= " ")
    # print(prifi.replace("Sagar","Lal Kumar"))
    # print(type(prifi))
    # print(prifi)
# lambda x, y: x+y
# lambda(5,6)

# freecodecamp
# my_range_var = range(5)
# print(my_range_var)
# print(isinstance("hello world",str))

# user_name: str = 'Moktan Sagar'
# print(user_name[1:9:3])

import os

# with open("sagar_1.txt", "w+") as file:
#     file.write("Hello From The Other Side>>.......\n")
#     file.write("This is sagar tamang form Nepal who is trying to learn AI and ML...")
#     file.write("\nthis is new line that i have made...")

# f = open("practice.txt","w+")
# f.write("""
#     Hi everyone
#     we are learning File I/O
#     using Java
#     I like programming in Java""")
# f.close()
# os.remove("moktnanew.txt")
# f = open("practice.txt","r")
# rep_sen = f.read()
# f.close()
# if rep_sen.find("learning"):
#     print("True")
# print(rep_sen.replace("Java","Python "))

# print("x" in "xyz")

#class is like a blueprint to make its objects
# variables or datas inside a class are called attributes 
# and the functions are called instances 

# class student:
#     #default constructor
#     # def __init__(self):
#     #     print("hello from the default constructor...")
#     #parameterized constructor
#     def __init__(self, name, age, address):
#         self.name = name 
#         self.age = age
#         self.add = address
#         print(self.name)
#         print(self.age)
#         print(self.add)
#         print()
#         # print(self)
#         # print('creating a constructor')
# s1 = student('moktan',20,'koteshwor')
# # print(s1)
# s2 = student('tamang',39, 'thimi')
# # print(s2)
# s3 = student('moktsagar', 50, 'kupondole')

# print(s3)
# print(s1)
# print(s1.name)
# s1.name = "moktan"
# print(s1.name)

# class human:
#     name = ""
#     cast = ""
#     age = 0
#     addrss = ""
#     # pri
#     # def work_job():
#     #     print("job is working")
# hum_1 = human()
# hum_1.name = "Sagar"
# hum_1.cast = "Tamang"
# hum_1.addrss = "Koteshwor"
# hum_1.age = 20
# print(hum_1.name, hum_1.cast, hum_1.age, hum_1.addrss)

