# def hello():
#     print("Gello")

# print(type(hello))
# print(type(1))
# print(type("hello"))
# print(type(33.43))

# class Dog:
#     def __init__(self, name):
#         pass
#     def meow(self):
#         return "mew!!!!"
#     def bark(self):
#         print("Bark!!!!!")
# do = Dog("Kali")
# do.bark()
# print(type(do))

# print(do.meow())

import time 

start_time = time.time()
print("hello@@@")
time.sleep(0.5)
print("end")
end_time = time.time()

print(f"{end_time -start_time}")
