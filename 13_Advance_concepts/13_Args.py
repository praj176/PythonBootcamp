'''
*args and **kwargs allow functions to accept a variable number of arguments.
'''
# *args lets you pass multiple positional arguments to a function.The arguments are stored as a tuple.
# **kwargs allows passing multiple keyword arguments. The arguments are stored as a dictionary.

def sum(*args):
    print(f"These are the arguments {args}.")
    total = 0
    for i in args:
        total += i
    return total

print(sum(2,5,21,54,23))
