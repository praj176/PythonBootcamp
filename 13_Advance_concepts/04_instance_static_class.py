'''
Static Method is a method inside a class that doesn't take self doesn't access instance or class data, and behaves like a regular function used for logical grouping.

'''

class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
e1 = Employee("Jack", 34500)
e2 = Employee("Jill", 36500)

print(Employee.company) #Class attribute / variable

print(Employee.name) #it is the attribute for the object/instance
        
