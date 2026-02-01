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

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.name, self.age)
#     def __del__(self): # distructor 
#         print("Object deleted or distructed")
    

# p = Person("Sagar", 44)


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other): 
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f" x "
    def __len__(self):
        return 50
    def __call__(self, *args, **kwrgs):
        print("Hello there i was called today...")
v1 = Vector(32,33)
v2 = Vector(33,22)
v3 = v1 + v2
print(v3.x, v3.y)
print(len(v3))
v3()
