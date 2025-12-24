import SmallProjects.passwordmodule as pm
while True:
#   my_password = input("Enter your password: ")
#   lenof_pass = len(my_password)
#   print(lenof_pass)
#   for i in range(lenof_pass):
#     if lenof_pass > 4:
#       print("strongenough")
#     else:
#       print("Not strong enough")

  # for i in my_password:
  #   print(i, end=" ")
  userpass = input("Enter your password(q to quit): ")
  if userpass == "q" or userpass == "Q":
    break 
  pm.final_count(userpass)
# pm.upper_count(userpass)