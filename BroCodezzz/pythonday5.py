# list comprehension

my_list = [1,3,2,34,45,34,23]
li = [a ** 2 for a in my_list if a % 3 == 0]
print(li)
print(my_list)
# print(45 ** 2)