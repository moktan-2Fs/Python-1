import bsignup as sn
import random as rd
import passwordmodule as pm
from blogin import Login as lg
import json


def file_open_read(*args, **kwargs):
    found = False
    try_again = 0
    with open("SmallProjects/credentials.txt", "r") as file:
        for line in file:
            obj = json.loads(line)
            if obj['id'] == kwargs['id'] and obj['password'] == kwargs['password']:
                print("successful Login.. Welcome to the program..")
                found = True
            elif obj['id'] == kwargs['id'] and obj['password'] != kwargs['password']:
                return 300
            else:
                continue
        if found:
            return 200
        else:
            return 404


def file_open_write(*args, **kwargs):
    with open("SmallProjects/credentials.txt", 'a') as file:
        json.dump(kwargs, file)
        file.write('\n')
        pass


print(" ---------- Welcome ----------\n ------ Bus Ticket System -----\n 1. Login \n 2. Signup")
user_ln = int(input("Choice: "))
if user_ln == 1:
    while_break = True
    while while_break:
        user_ln_id = input("Id: ")
        user_ln_pass = input("Password: ")
        fail = False
        if file_open_read(id=user_ln_id, password=user_ln_pass) == 1:
            print('Welcome')
            break
        elif file_open_read(id=user_ln_id, password=user_ln_pass) == 5:
            change_pass = input("Forgot password?(Y/N): ")
            if change_pass in 'yY':
                new_pass = input("Password: ")
        else:
            print("fck. try again")

elif user_ln == 2:
    while True:
        comp_str = "abcdefghijklmnopqrstuvwxyz0123456789@#!$%&*ABCDEFGHIJKLMN?OPQRSTUVWXYZ"
        user_id_list = rd.choices(comp_str, k=10)
        user_id = ''.join(user_id_list)
        user_email = input("Email: ")
        obj1 = lg(user_email, user_id)
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
