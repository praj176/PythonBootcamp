'''
Python provides three types of dictionary view objects:

dict.keys() – Returns a view of all keys.

dict.values() – Returns a view of all values.

dict.items() – Returns a view of key-value pairs as tuples.
'''

student = {"name": "Richard", "age": 34, "grade": "A"}

print(student.keys()) # prints all the keys present in the dictionary

print(student.values()) #prints all the values present in the dictionary

print(student.items()) #Returns a view of key-value pairs as tuples.

student.pop("name") #Pops/ deletes the KEY and the associated value given to the pop function

# student.clear() # Clears all the dictionary elements

print(student)

