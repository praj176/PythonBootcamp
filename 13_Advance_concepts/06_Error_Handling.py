'''
Errors and exception handling in Python help ensure that a program can gracefully recover from unexpected issues.
Types of Errors:
- Syntax Errors
- Runtime Errors (Exceptions) – Occur while the program is running (e.g., dividing by zero, accessing an invalid index).
'''

while True:
    # Try and except statements are used to handle programs in python.
    '''
    Whenever there is an error, the code inside the accept block is executed and if there is no error the code inside the try block will be executed
    '''
    try:
        a = int(input("Enter the first number? "))
        b = int(input("Enter the second number? "))
        print(f"The sum of both number is {a + b}")

    except:
        print("Some error occurred")
    
