'''
Static Method is a method inside a class that doesn't take self doesn't access instance or class data, and behaves like a regular function used for logical grouping.

Instance Method: Talks about that one object uses self as the first parameter. default method

Class Method: Talks about the whole class — uses cls.

'''

class Employee:
    # Class variable shared by all employees
    company = "HP"

    def __init__(self, name, salary):
        # Instance variables unique to each employee
        self.name = name
        self.salary = salary

    # Instance method: uses 'self' to access object data, default method
    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    # Static Method is a method which doesn't need self parameter.
    @staticmethod
    def sum(a, b):
        return a + b

    # Class method: uses 'cls' to access or modify class-level data
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


# Creating employee objects
e1 = Employee("Jack", 34500)
e2 = Employee("Jill", 36500)

# Accessing class variable
print(Employee.company)

# Accessing instance methods
e1.print_info()
e2.print_info()

# Using static method
print(Employee.sum(4, 5))

# Using class methods
e1.prin

