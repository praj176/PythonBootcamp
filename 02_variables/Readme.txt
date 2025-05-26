# Python Variables 📌

Variables in Python act as **containers for storing data**. Python is a **dynamically typed language**, meaning you don't need to declare a variable type—it automatically detects it.

## 🔹 Creating Variables
Assign values using the `=` sign:
```python
x = 5      # Integer variable
y = "Hello"  # String variable
z = 3.14   # Float variable

🔹 Naming Rules
✅ Start with a letter or _ ✅ Cannot start with a number ✅ Can contain letters, numbers, _ ✅ Case-sensitive (name ≠ Name)

🔹 Changing & Assigning Variables
x = 10  # Change value
a, b, c = 1, 2, 3  # Multiple assignment

🔹 Checking Data Type
num = 10
print(type(num))  # <class 'int'>

🔹 Scope: Global vs. Local Variables
def my_function():
    local_var = "Local"
    print(local_var)

global_var = "Global"
print(global_var)

🔹 Built-in Data Types
Integer → Whole numbers

Float → Decimal numbers

String → Text data

Boolean → True or False

List → [1, 2, 3] (Ordered, Mutable)

Tuple → (1, 2, 3) (Ordered, Immutable)

Set → {1, 2, 3} (Unordered, Unique)

Dictionary → {"name": "Alice", "age": 25} (Key-value pairs)
