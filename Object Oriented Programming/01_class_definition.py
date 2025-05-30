# OOP
# Object-Oriented Programming (OOP) is a programming paradigm in Python that revolves around objects and classes. 
# It helps structure code in a more organized, reusable, and modular way, making large programs easier to maintain.

#An object is a real-world entity with attributes (data) and behaviors (methods). 
# A class is a blueprint/template for creating objects. eg. Car
#An Object is the special instance of the class eg. Audi Q4
# We create classes so that we can model our program just like real world instances

class Employee:
    company = "Happy"
    
    def salary(self): # When you create an object in Python, that object has its own data. 
                        # The keyword self helps a class refer to its own data.
                        # Self references to the object which is being talked about at that particular time
        return 40000
    
e = Employee() #Object of class employee is created here

print(e.salary()) # Employee e gets the salary of 40000

e2 = Employee()

print(e2.company,e2.salary())
