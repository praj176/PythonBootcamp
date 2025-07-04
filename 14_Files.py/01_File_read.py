'''
We can read-write and append a file
Working with files generally involves:
1. Opening a file
2. Performing operations
3. Closing the file
'''
#in-order to read a file we need to create a file object
f = open("14_Files.py\\test.txt", "r") 
#Use relative path or the absolute path of the file and at last try to use double backward slashes (\\) instead of one to avoid Syntax errors for escape characters 
content = f.read()
print(content)
f.close()

#Exception if in case the file is not found in the location.
except FileNotFoundError: # Name of the error which is faced when the file is not found
  print("File not found")

'''
if we need to read a file line by line
>> Efficient for large files

for line in file:
  print(line) #To print just the line
  print(line.strip()) #Removes the inline characters
file.close() 
'''
