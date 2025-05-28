def sum(a,b): # a and b are called parameters
    return a + b

#Positional Arguments

total = sum(5,1) # 5 and 1 are called the arguments
print(total)

#Default Arguments

def greet(name = "Guestt"):
    return f"Hello, {name}"

print(greet()) #Output Hello, Guestt

#Keyword Arguments

# Keyword arguments in Python let you pass values to a function using the parameter names.

def greet(name, age):
    print(f"My name is {name} and I am {age} years old.")

# Using keyword arguments
greet(age=25, name="Alice")  # Works fine even if order is changed!
