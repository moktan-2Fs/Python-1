# class Person:
#   def __init__(self,name,age,gen,nation_id):
#     self.name = name
#     self.age = age
#     self.gen = gen
#     self.nat_id = nation_id
  
#   def nationality(self):
#     return self.nat_id
rows = 5

for i in range(1, rows + 1):

    # spaces
    for s in range(rows - i):
        print(" ", end="")

    # stars 
    for k in range(2 * i - 1):
        print("*", end="")

    print()
