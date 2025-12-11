# #while and for loops i python
# print("hello")
# count = 0
# while count < 10:
#   print("moktan",count)
#   count += 1
# print(count)
# num = 0
# while num < 5:
#   print("the number is:",num)
#   num += 1
# k =  int(input("Enter the number for its multiple: "))
# i = 1
# while i<= 10:
#   mul = k*i
#   print(mul)
#   i += 1
# i = 0
# my_list = [1,3,3,4,5,3,6454,4534,34,34,342,2,32,64,433]
# print(len(my_list))
# while i <= len(my_list)-1:
#   print(my_list[i], i)

#   i += 1
# i = 1
# my_string = ["moktan","rohan","sohan","mohan"]
# while i < len(my_string):
#   print(my_string[i])
#   i += 2

# my_list = (1,3,3,4,5,3,6454,4534,34,34,342,2,32,64,433)
# i = 0
# x = 34
# while i < len(my_list):
#   if my_list[i] == x:
#     print(i , my_list[i])
#   i += 1

# i = 1
# while i <= 5:
#   print(i)
#   if (i == 4):
#     break
#   i += 1

# i = 0
# while i<=5: #this is an example of while loop in python
#   if(i==3):
#     i += 1
#     continue
#   print(i)
#   i += 1

# import math
# radius = float(input("Enter the radius of the circle: "))
# area = 2*math.pi*pow(radius, 2)
# print(f"The area of the circle is: {area}")

# response = input("Whold you go out on a date with me?(Y/y|N/n)").strip()
# if response == "N" or response == "n":
#     print("It's fine. It was good to know you.")
# elif response == "Y" or response == "y":
#     print("Great lets do that next Saturday..")
# else:
#     print("Its good to know that and yeah its ok..")
# if response == "":
#     print("you didnt type anything")
# else:
#     print("its alright..")

# for_sale = False
# if for_sale:
#     print("You are for sale..")
# else:
#     print("Not for sale...")

#calculator in python
# oper = input("Enter any operator to perform the task: ")
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2nd number: "))
# result = None
# if oper == "":
#     print("Enter a valid ")
# if oper == "+":
#     result = num1 + num2 
# elif oper == "-":
#     result = num1 - num2 
# elif oper == "/":
#     result = num1 / num2
# elif oper == "%":
#     result = num1 % num2
# elif oper == "*":
#     result = num1 * num2
# else:
#     print("Please enter a valid operator...")
# print("The final result is: ", result)
try:
    ab = int(input("Enter any number: "))
    ba = int(input("Enter any number: "))
    print(ab + ba)
except ZeroDivisionError:
    print("cannot divide by 0 you jackass")
except TypeError:
    print("cannot perform operations on different types")
except ValueError:
    print("Please enter a valid number Mr. Jackass")
except Exception:
    print("it is whole and all types of exception") # this takes all errors and works on them not good for use 
finally:
    print("this is executed after the except are executed")
# print(ab/0) #ZeroDivisionError 
# print("ke" + ab) # typeerror , valueerror is when user enters different datatype like strings instead of integars

