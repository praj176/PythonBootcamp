'''
Object introspection in Python simply means checking an object's details while the program is running. It helps you find out things like:

What type is the object? → type(obj)

Where is it stored? → id(obj)

What functions or properties does it have? → dir(obj)

Does it have a certain attribute? → hasattr(obj, "attribute_name")

Get the value of an attribute → getattr(obj, "attribute_name")

Is it an instance of a specific class? → isinstance(obj, ClassName)'''

class Employee:
    company = "HP"
    
    def __init__(self , name, salary , bond, location, company):
        self.salary = salary # Create a instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.location= location
        self.company = company
    
    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee {self.name} and the salary is {self.salary} working from {self.location} for the tenure of {self.bond} years.")
        
e1 = Employee("Mahesh", 30000, 1, "Mumbai", "IBM")
e1.get_info()

print(Employee.company)

e2 = Employee("Ramesh", 30300, 2, "Juhu", "AMazon")
e2.get_info()

print(e1.__dir__())
