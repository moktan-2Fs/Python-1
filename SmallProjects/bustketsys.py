import bsignup as sn 
import passwordmodule as pm 
from blogin import Login as lg

print(" ---------- Welcome ----------\n ------ Bus Ticket System -----\n 1. Login \n 2. Signup")
user_ln = int(input("Choice: "))
if user_ln == 1:
  while True:
    user_email = input("Email: ")
    user_num = input("Number: ")
    obj1 = lg(user_email,user_num)
    if obj1.is_valid_email and obj1.is_valid_number:
      print("Valid email and valid number.")
      break
    else:
      print("Invalid \nTry again. ")

  while True:
    user_pass = input("Password: ")
    if pm.final_count(user_pass):
      print("The password is very strong.")
      break
    else:
      print("Weak Password. \nTry stronger password..")


# while True:
#   user = int(input("Input: "))
#   if user == 1:
#     print(" ---------- Welcome ----------\n ------ Bus Ticket System -----")
#     print(" 1. View Available Buses \n 2. Bus Routes \n 3. Ticket Available \n 4. Exit ")
#     use_choi = int(input("Enter your choice: "))
#     match use_choi:
#       case 1:
#         with open("buses.txt", "w+") as file:
#           pass
#       case 2:
#         pass
#       case 3:
#         pass
#       case _:
#         pass
#   else: 
#     pass