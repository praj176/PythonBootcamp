'''
>> filter(function, iterable)
Filters elements in the iterable for which the function returns True.
'''

def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False
    
a = [2,6,4,12,6,21,67,11]

new = filter(is_greater_than_9,a)
print(new)
print(list(new))

'''
Filter function is used to create a new list or a new filter object only for those values for which the function is True
'''
