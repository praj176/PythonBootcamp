'''
Map, Filter and Reduce are higher-order functions in Python which operate on iterables (LIST, TUPLES, etc)

> map(), filter(), and reduce() are powerful built-in functions in Python that let you process and transform data in elegant, functional ways.
'''

# map(function, iterable)
# Applies a function to every item in an iterable (like a list) and returns a map object (which can be converted to a list).

numbers = [1,2,3,4,12,34,25]

def square(x):
    return x * x

# The square function is applied to each and every iterable in the list!
new = list(map(square, numbers))
print(new)
