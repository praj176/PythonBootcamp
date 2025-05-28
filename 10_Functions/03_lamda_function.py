# Lambda functions in Python are small, anonymous functions that you can define using the lambda keyword. 
# They are often used for short operations where defining a full function with def would be unnecessary.
# One liner function required when we want to pass a function to a function

# lambda arguments: expression


square = lambda x : x**2
sum = lambda x,y : x + y

print(square(2))
print(sum(34,45))

