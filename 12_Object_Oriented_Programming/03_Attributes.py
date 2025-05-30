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
