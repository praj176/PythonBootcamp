'''
**kwargs allows passing multiple keyword arguments.

The arguments are stored as a dictionary. In a form of key-value pair
'''

def print_details(**kwargs):
    for key, value in kwargs.items(): #.items() method in Python returns a view object that contains key-value pairs from a dictionary as tuples.
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")

