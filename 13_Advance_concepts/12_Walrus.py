'''
Walrus operator is := is an assignment expression operator which allows you to assign a value to a variable within an expression
> makes code concise, avoids repeated function calls
'''
'''
>> Without walrus operator

list = [1, 2, 3, 4, 5]
n = len(list)
while n > 0:
    print(numbers.pop())
    n = len(numbers)
'''

#With the Walrus operator

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

''' ALT Example 
Without walrus operator

name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")

With Walrus Operator

if (name := input("Enter your name: ")):
    print(f"Hello, {name}!")

Walrus operator helps in assigning value to a variable within an expression ('if' in this case)
'''
