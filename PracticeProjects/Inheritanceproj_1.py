# class Store():

#     def __init__(self, name, location, size):
#         self.name = name
#         self.location = location
#         self.size = size

#     def details_store(self):
#         return f"\nName: {self.name} \nLocation: {self.location} \nSize: {self.size}"

# class Financialdetailstore(Store):

#     def __init__(self,name,location,size,netsales,totalexpenses):
#         super().__init__(name,location,size)
#         self.netsales = netsales
#         self.totalexpenses = totalexpenses

#     def netprifitloss(self):
#         return self.netsales - self.totalexpenses

# obj = list()
# dicty = {}
# data = ()
# no_of_stores = int(input("Enter the number of stores: "))
# print("Enter the details of the store:")
# for i in range(no_of_stores):
#     name = input('Name: ')
#     location = input("Location: ")
#     size = input("Size: ")
#     objct = Store(name, location, size)
#     choi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     dicty[choi[i]] = objct

# for keys, values in dicty.items():
#     print(keys, values.details_store())

