import passworddecoder as pd
import random as rd
import string as st
import passwordmodule as pm
while True:
  print("\n----------Welcome User!----------\n")
  print(" 1. Encode Password \n 2. Decode Password \n 3. Check Password Strength \n 4. Exit Program")
  usr_choi = int(input("\nPlease enter your choice: "))
  if usr_choi == 4:
    break
  # elif usr_choi == 3:
  #   userpass = input("\nEnter your password:): ")
  #   pm.final_count(userpass) 
  elif usr_choi == 2:
    pass
  else:
    user_password = input("Enter your password for decoding: ").strip()
    list_user = [] 
    rand_list = []
    for char in user_password:
      list_user.append(char)
      ran_bina = rd.randrange(0,999999)
      rand_list.append(ran_bina)
    print(list_user)
    print(rand_list)
    with open("passwordlist.txt","w+") as file:
      for li in list_user:
        fi = li
        file.write(fi)
        file.write(",")
      file.write("\n")
      for ran in rand_list:
        ran = str(ran)
        file.write(ran)
        file.write(",")