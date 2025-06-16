'''
reduce(function, iterable) :
Takes a list and combines its items one by one into a single value using a function you provide.
Applies a rolling computation to sequential pairs of items.
'''
from functools import reduce

list = [1,2,3,4,5,6]

def sum(a,b):
  return a + b

c = reduce(sum, list)
print(c)
