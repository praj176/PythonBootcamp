# decorator in Python is a function that takes another function as input, 
# adds some functionality to it, and returns a new function—without modifying the original function's code.

def decorator(func):
    def wrapper(): #This is the "wrapped" function that adds extra behavior.It: Prints a line before > Calls the original func() (whatever function was passed in) > Prints a line after
        print("Let's print Hello here")
        func()
        print("I have printed the funct()")
    return wrapper()

#Decorator is a function that takes a function > then it creates a new function in it's body(wrapper)
# Then it returns that new function


# def say_hello():
#     print("hello!")
    
# say_hello()

# ####### traditional approach to call the decorator function

# deco  = decorator(say_hello)
# deco

# Original syntax which is ususally used
@decorator 
def say_hello():
    print("hello!")
    
''' It syntactically means say_hello= decorator(say_hello)
it modifies the behavior of the say_hello by wrapping it inside the wrapper()
'''
