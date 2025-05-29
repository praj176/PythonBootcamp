#Docstrings are used to document functions, classes and modules in Python.
#A docstring is written using triple quotes (""" """) or (''' ''') and is placed at the beginning of a function or class.

def sum(a,b):
    '''This will add two int'''
    c = a + b
    return c

print(sum.__doc__)
