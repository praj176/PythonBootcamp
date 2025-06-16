'''
Map, Filter and Reduce are higher-order functions in Python which operate on iterables (LIST, TUPLES, etc)
'''

numbers = [1,2,3,4,12,34,25]

def square(x):
    return x * x

# The square function is applied to each and every iterable in the list!
new = list(map(square, numbers))
print(new)