#A module in Python is a file containing reusable code like functions, classes, or variables.
# we could leverage someone's code by importing the module using the import function
# Built in modules in python : https://www.geeksforgeeks.org/built-in-modules-in-python/

import math
import os
import mymodule
import requests
print(math.sqrt(16))

#creating own module
mymodule.hey()

#external modules

# can be installed using pip

# pip install requests >>> in the terminal

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
