class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gndr = gender

    def stud(self):
        print(f'{self.name} studies in New York..')

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gndr}"


class Worker(Person):

    def __init__(self, name, age, gender, salary):
        super(Worker, self).__init__(name, age, gender)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += f', Salary: {self.salary}'
        return text

    def stud(self):
        print("hello mro")
        super().stud()
        print(f"this is from {self.name}")

    def calc_salary(self):
        return self.salary * 12


worker1 = Worker('kumar', 40, "M", 60000)
print(worker1)
print(worker1.calc_salary())
print(worker1.stud())


#Operator Overloading

class Vector():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"
    
v1 = Vector(31,44)
v2 = Vector(44,32)
print(v1)
print(v2)
v3 = v1 + v2 
print(v3)
v3 = v1 - v2
print(v3)