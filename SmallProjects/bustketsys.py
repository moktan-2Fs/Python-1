import bsignup as sn 
import random as rd
import passwordmodule as pm 
from blogin import Login as lg
import json

print(" ---------- Welcome ----------\n ------ Bus Ticket System -----\n 1. Login \n 2. Signup")
user_ln = int(input("Choice: "))
if user_ln == 1:
  while_break = True
  while while_break:
    user_ln_id = input("Id: ")
    # while True:
    #   user_ln_email = input("Email: ")
    #   ln_email = lg(user_ln_email,user_ln_id)
    #   if ln_email.is_valid_email():
    #     break
    #   else:
    #     print("Enter a valid email. Jackass !!!")
    #     continue
    user_ln_pass = input("Password: ")
    fail = False
    with open("SmallProjects/credentials.txt", 'r') as file:
      for line in file:
        ln_obj = json.loads(line)
        if ln_obj['id'] == user_ln_id and ln_obj['password'] == user_ln_pass:
          print(ln_obj)
          print("login successful!!!!1")
          while_break = False
          break
        else:
          fail += 1
          continue
      if while_break == True:
        print("login NOt done")
    pass

elif user_ln == 2:
  while True:
    comp_str = "abcdefghijklmnopqrstuvwxyz0123456789@#!$%&*ABCDEFGHIJKLMN?OPQRSTUVWXYZ"
    user_id_list= rd.choices(comp_str,k=10)
    user_id = ''.join(user_id_list)
    user_email = input("Email: ")
    obj1 = lg(user_email,user_id)
    if obj1.is_valid_email(): 
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
  print(f"Hye \'{user_id}\' is your Id. Keep it secure and noted, it's required for login into the system...")
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