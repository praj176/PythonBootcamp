#List comprehension in Python is a concise way to create lists using a single line of code. 
# It allows you to generate lists from existing iterables like lists, tuples, or ranges, using a clear and readable syntax.


#create a list containing a table of 5
# table = []
# a = 5
# for i in range(1,11):
#     table.append(5*i)

# print(table)

# Using List comprehension

table = [5*i for i in range(1,11)]

print(table)
