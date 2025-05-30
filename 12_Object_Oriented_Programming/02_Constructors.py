class Employee:
    company = "Happy"
    
    def __init__(self , name, salary , bond, location):
        self.salary = salary # Create a instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.location= location
        pass
    
    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee {self.name} and the salary is {self.salary} working from {self.location} for the tenure of {self.bond} years.")


e1 = Employee("Kaka Patil", 50000, 2, "Pune")

print(e1.get_salary())
e1.get_info()
