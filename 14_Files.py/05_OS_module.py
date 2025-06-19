'''
Python's OS module provides functions for interacting with the operating system, such as working with directories and files
'''
import os

#we can get the content of the directory
a = os.listdir("14_File_IO.py//dir")   
print(a)

b = os.getcwd() # cwd = current working directory
print(b)

print(os.path.exists("test_dir")) # check is the mentioned directory is present in the current directory
#Returns TRUE/FALSE

#To delete a file
os.remove("#path")

#To delete EMPTY directory
os.rmdir()
#To delete Non-empty directory we need to use shutill module

#To rename the file or Directory
os.rename(old_name.txt, new_name.txt)
