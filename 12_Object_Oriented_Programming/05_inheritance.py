# Inheritance is like a family tree. 
# A class(child) inherits traits(attributes(data) and methods(actions)) from it's parents class(superclass)
# This allows us to create new classes with specialized versions of existing classes without rewriting all the code again

class Animal:
    msg = "Listen carefully > "
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print("Animal sound")
        
    def test(self):
        print("Super case")
        
class Dog(Animal):
    def speak(self):
        super().test() # we are using the test function from the Animal class using super()
        print("Woof!")
    
a = Animal("Dog")
a.speak()

d = Dog("Kuttu")
print(f"the name of dog is {d.name} and now {d.msg}")
d.speak()
