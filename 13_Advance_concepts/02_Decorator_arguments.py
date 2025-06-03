'''
Decorate themselves can also accept arguments. 
This requires another level of nesting > An outer function that takes the decorator's arguments and returns the actual decorator funtion

A normal decorator adds functionality, but sometimes we need custom settings like timeouts or logging levels.
To achieve this, decorators use extra nesting:
1. Outer function → Takes arguments (e.g., timeout duration).
2. Middle function → Applies changes as the actual decorator.
3. Inner function → Wraps the target function to modify its behavior.

This makes decorators customizable!

'''
def repeat(n): #repeat function is returning the decorator
    def decorator(func):
        def wrapper(a): # Wrapper fucntion is returning the output by running for n times
            for i in range(n):
                func(a)
        return wrapper  
    return decorator    

@repeat(7) #decorating the fucntion say_hello() where n is 7
def say_hello(a): # func > say_hello where a = Check
    print(f"hello {a}")

say_hello("Check")
