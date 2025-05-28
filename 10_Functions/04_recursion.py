#Recursion : A function calling itself to solve a problem

#Note : You must have a base case to avoid infinite recursion


# Fibonacci series 
# 0  1  1   2   3   5   8   13   21   34  55  89  144 .............
# 0  1  2   3   4   5   6   7    8    9   10  11   12 .............

def fib(n):
    if(n == 0 or n == 1):
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Please input the nth place number in the fibonacci series : "))
print(fib(n))

# Factorial 
# 4! = 4 x 3! = 4 x 3 x 2! = 4 x 3 x 2 x 1!

def factorial(a):
    if a== 0 or a == 1:
        return 1
    return a * factorial(a-1)

a = int(input("Enter the number of which factorial you want : "))
print(factorial(a))

