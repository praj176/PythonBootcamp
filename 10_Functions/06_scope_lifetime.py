# Function Scope and Lifetime in Python
# In Python, scope refers to the visibility and accessibility of variables, while lifetime refers to how long a variable exists in memory.

# Local Scope: Variables inside a function, accessible only within it.
# Global Scope: Variables declared outside any function, accessible throughout the script.

#Variables are created when a function is called and destroyed when it returns

def sum(a,b):
    c = a + b
    z = 1 # it is a local variable which is destroyed after this function return
    return c


z = 8 # Global variable

print(sum(4,5))

# print(a)
# print(b)
# print(c)
print(z)

#Using the global keyword
# to modify the a global variable inside a function, use the global keyword

