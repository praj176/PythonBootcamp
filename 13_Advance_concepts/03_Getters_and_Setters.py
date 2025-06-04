'''
Setters and Getter used for writting cleaner syntax which are the key part of ENCAPSULATION
Setters and getters are special methods used in object-oriented programming to control access and modify your class attributes.

> Getter: A method that RETRIEVES (gets) the value of an attribute.
Setter: A method that MODIFIES (sets) the value of an attribute while ensuring valid data.

They help protect data, enforce constraints, and maintain clean code.
Used along with : Property decorator > Makes the method act like an attribute
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    #function to return the first name of the full name by using the split method on string
    #03.2 Adding property decorator to Make the method act like an attribute
    @property
    def first_name(self):
        return self.name.split(" ")[0] 
        # Splits the strings from the space character and stores in a list and then returns the first index.
        '''
        This means > l = self.name.split(" ")
        print(l) > prints the list.
        return l[0] > returns the first element
        '''
        
    #03.1 function to change just the first name
    # def new_name(self,fname):
    #     l = self.name.split(" ")
    #     new = f"{fname} {l[1]}"
    #     self.name = new
    
    #03.2 the above function can we written using setter
    @first_name.setter
    def first_name(self,fname):
        l = self.name.split(" ")
        new = f"{fname} {l[1]}"
        self.name = new
    
e = Employee("Ramesh Kaka", 32000)
print(e.name)
# print(e.first_name())

# 03.2 after adding @propert decorator
print(e.first_name)


# Point 03.1 we are exploring if there is anyway to change just the first name of the person
# check the function new_name function above

# e.new_name("Paresh")
# print(e.name)

'''
03.2
instead of making so many calling of function calls we can use property decorators
A property decorator (@property) is a built-in Python feature that allows you to define a method that behaves like an attribute.
a method (a function inside a class) can be accessed like a variable instead of being called with parentheses.

Makes the method act like an attribute
'''

e.first_name = "Paresh"  # Works like an attribute now!
print(e.name)  #  Prints updated name "Paresh Kaka"
