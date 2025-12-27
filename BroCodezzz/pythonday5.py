# list comprehension
# my_list = [1,3,2,34,45,34,23]
# li = [a ** 2 for a in my_list if a % 3 == 0]
# print(li)
# print(my_list)
# # print(45 ** 2)

# task 1

# print("Enter the number you want to add in the list: \n")
# while True:
#     add_no = int(input())
#     try:
#         if add_no == "q" or add_no == "Q":
#             break
#         else:
#             orig_list.append(add_no)
#     except ValueError:
#         print("There was an error related to the value you entered....")
#     finally:
#         print("try again.....")


# orig_list = []
# print("Enter the number you want to add in the list(11111 to quit): ")
# while True:
#     num_user = int(input())
#     if num_user == 11111:
#         break
#     orig_list.append(num_user)
# for num in orig_list:
#     if num > 10:
#         print(num, end= " ")


# # q2 

# user_str = input("Enter any string: ")
# use_list = [vowl for vowl in user_str if vowl in "aeiou"]
# for use in use_list:
#     print(use)

use = "amgno"
if use in "kikamgno":
    print("hello")
else:
    print('byeeeee')
