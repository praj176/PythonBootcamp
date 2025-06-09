'''
Dunder methods (also called magic methods) are special methods in Python with names having double underscores like __init__, __str__, and __add__.
  > They let you customize how your objects behave with built-in operators, functions, and language features.
  > They make your classes more intuitive, powerful, and Python —supporting things like operator overloading, custom string output, and more.
'''
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)


e = Employee("Harry", 43566)
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))
