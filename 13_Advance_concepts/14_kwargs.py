'''
**kwargs allows passing multiple keyword arguments.

The arguments are stored as a dictionary. In a form of key-value pair
'''

# def print_details(**kwargs):
#     for key, value in kwargs.items(): 
# #   The .items() method in Python returns key-value pairs from a dictionary as tuples in a view object.
#         print(f"{key}: {value}")

# print_details(name="Alice", age=25, city="New York")

def school(**kwargs):
    #kwargs is a dictionary with all the key value pair which is passed to kwargs
    print(kwargs.keys())
    for item in kwargs.keys():
        print(f"Parameters are {item} and value for them are {kwargs[item]}") 
        #kwargs[item(#which are the keys in this case)] retrieves the value associated with that key.
        
school(name = "Jeju", age = 45, location = "Nashik")

'''
Output :
dict_keys(['name', 'age', 'location'])
Parameters are name and value for them are Prajwal
Parameters are age and value for them are 45
Parameters are location and value for them are Nashik
'''
