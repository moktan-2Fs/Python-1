import json
import random as rd
# def email1(email):
#   fou = False
#   for em in email:
#     if em == '@':
#       fou = True
#     else:
#       continue
#   if email[len(email)-4: len(email)] == ".com" and fou == True:
#     print("the email is valid.")

# email1("sagarmoktan@gmail.com")
# # email = "sagarmoktan@gmail.com"
# # print(email[len(email)-4: len(email)])
# strin = "abcdefghijklmnopqrstuvwxyz0123456789@#!$%&*"
# rand_id = rd.choices(strin,k=7)
# final_id = ''.join(rand_id)
# print(type(final_id))
# print(final_id)
# print(rand_id)
# # data = {
#     "id": 1,
#     "name": "sagar",
#     "cast": "tamang"
# }
# with open("creds.md", "a") as file:
#     json.dump(data, file)
#     file.write("\n")
# import json
# with open("SmallProjects/credentials.txt","r") as file:
#     for line in file:
#         obj = json.loads(line)
#         for keys,values in obj.items():
#             print(keys,"=",values)
#         print(type(obj),obj)


# def kwar(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# kwar(name ='sagar', password = 'alfjsdfj',email= 'sagar@gmail.com')

# def file_open_write(*args, **kwargs):
#     with open("SmallProjects/credentials.json", 'a') as file:
#         json.dump(kwargs, file)
#         file.write('\n')

# file_open_write(name='Sagar Moktan', email='sagarmoktan@gmail.com',password='maoktanSF242@')   
def id_generator():
    id_chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&'
    id= ''.join(rd.choices(id_chars,k=10))
    print(id,type(id))

id_generator()