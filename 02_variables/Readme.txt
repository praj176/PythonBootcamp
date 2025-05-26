Python Variables
A variable is a container for storing data values. 
In Python, we don't need to declare a variable type; 
Python automatically detects it as Python is a DYNAMICALLY TYPED LANGUAGE.

Creating Variables: We create a variable by assigning a value to it using the = sign.

x = 5    # Integer variable
y = "Hello"  # String variable
z = 3.14  # Float variable

Variable Naming Rules:

Must start with a letter or underscore (_)

Cannot start with a number

Can contain letters, numbers, and underscores

Case-sensitive (name and Name are different)

Changing a Variable's Value: Python allows you to reassign a variable.

python
x = 10  # Now x holds 10 instead of 5
Multiple Variable Assignment: You can assign multiple variables at once.

python
a, b, c = 1, 2, 3
Variables and Data Types: Python supports various data types, and you can check a variable's type using type().

python
num = 10
print(type(num))  # Output: <class 'int'>

Global vs. Local Variables: Variables declared inside a function are local, while those outside are global.

python
def my_function():
    local_var = "I am local"
    print(local_var)

global_var = "I am global"
print(global_var)

# Built-in data-types in Python
1. Integer
2. Float
3. String
4. Boolean
5. List : Ordered, mutable collection of datatype (eg. [1,2,3])
6. Tuples : Ordered, Immutable collection of datatype variable (eg. (1,2,3))
7. Sets : Unordered collection of unique elements (eg. {1,2,3})
8. Dictionary : key Value pairs (eg. {"name" : "Alice", "age" : 25})

