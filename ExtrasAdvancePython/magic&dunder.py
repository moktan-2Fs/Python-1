# class Person:
#     def __init__(self):
#         pass
#     def data_person(self,**kwargs):
#         self.keyargs = kwargs
#         print(self.keyargs)
# obj = Person()
# con = True
# data_key = list()
# print('Enter all the keys(q to quit):')
# i = 1
# while con == True:
#     data_key.append(input(f'{i}: ').lower().strip())
#     if i == 2:
#         con = False
#     i += 1
# print(data_key)
# data_value = list()
# i = 0
# for key in data_key:
#     data_value.append(input(f"{data_key[i]}: ").lower().strip())
#     i += 1
# print(data_value)
# print(data_key)
# data_dict = dict()
# print(type(data_dict))
# i = 0
# for valuse in data_key:
#     data_dict[valuse] = data_value[i]
#     i += 1
# print(data_dict)
# obj.data_person(data_dict)



# # Dunder -> used or declared using __ladfj__



for i in range(5):
    if i ==3: break
print(i)
