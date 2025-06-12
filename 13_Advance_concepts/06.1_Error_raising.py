'''
Raising/Throwing an error

'''

a = int(input("Enter the first number? "))
b = int(input("Enter the second number? "))

#before the error occurs
if b == 0 :
  raise ValueError("Please don't divide by zero")
print(f"The division of both number is {a / b}")
