class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
e1 = Employee("Jack", 34500)
e2 = Employee("Jill", 36500)

print(Employee.company) #Class attribute / variable

print(Employee.name) #it is the attribute for the object/instance
        
