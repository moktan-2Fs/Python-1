class Person:
    amount = 0 # this is like a global var, can be accessed with the class name and is same for alll the objects 

    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.amount += 1 # amount increases each time a object of the class is created 

    def helloworld(self):
        print("slfjsjfjslf")

    def __str__(self): # to deliver a string when the object is printed 
        return (f"This is {self.name}s object.")
    
    def get_older(self,years):
        self.age += years


x = Person('sagar',20,"M")
print(x.name,x.age,x.gender)
x.helloworld()

y = Person('roshan',22, "M")
print(y.name,y.age,y.gender)
y.helloworld()

print(x)
print(y)
print(Person.amount)

