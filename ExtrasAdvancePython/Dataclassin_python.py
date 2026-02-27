from dataclasses import dataclass

@dataclass # populates the default methods like __init__, __repr__, __eq__ etc.
class Moktan:
    name: str
    age: int 

p1 = Moktan("Sagar", 22)
p2 = Moktan("Raj", 21)

print(p1, p2, end='\n')
print(p1 == p2)
print(p1.name, p2.age)

@dataclass
class Employee:
    name: str
    department: str
    id: int = 0

    def operation(self) -> str:
        return f"{self.name} is working in {self.department} and is a very good friend of mine. Also, he is about to with the best employee of the year award."

employes = []
for _ in range(2):
    name = input("Enter employee name: ")
    id = int(input("Enter employee id: "))
    department = input("Enter employee department: ")
    emp = Employee(name, id, department)
    employes.append(emp)

print(employes)
for emp in employes:
    print(emp.name, emp.id, emp.department)
    print("\n") 