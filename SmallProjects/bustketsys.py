import bsignup as sn 
import random as rd
import passwordmodule as pm 
from blogin import Login as lg
import json

print(" ---------- Welcome ----------\n ------ Bus Ticket System -----\n 1. Login \n 2. Signup")
user_ln = int(input("Choice: "))
if user_ln == 2:
  while True:
    comp_str = "abcdefghijklmnopqrstuvwxyz0123456789@#!$%&*ABCDEFGHIJKLMN?OPQRSTUVWXYZ"
    user_id_list= rd.choices(comp_str,k=7)
    user_id = ''.join(user_id_list)
    user_email = input("Email: ")
    obj1 = lg(user_email,user_id)
    if obj1.is_valid_email:
      print("Valid email.")
      break
    else:
      print(" Invalid!!Try again. ")

  while True:
    user_pass = input("Password: ")
    if pm.final_count(user_pass):
      print("The password is very strong.")
      break
    else:
      print("Weak Password. \nTry stronger password..")
  user_detail = {
    "id": user_id,
    "email": user_email,
    "password": user_pass
  }
  with open("SmallProjects/credentials.txt", "a") as file:
    file.write(json.dumps(user_detail) + "\n")


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