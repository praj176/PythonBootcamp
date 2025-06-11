'''
Errors and exception handling in Python help ensure that a program can gracefully recover from unexpected issues.
Types of Errors:
- Syntax Errors
- Runtime Errors (Exceptions) – Occur while the program is running (e.g., dividing by zero, accessing an invalid index).

ZeroDivisionError	>  Division by zero (10 / 0)
TypeError           >  Invalid operation between incompatible types ("text" + 5)
IndexError          >  Accessing an out-of-range list index (lst[10] when lst has 5 elements)
KeyError	        > Trying to access a non-existent dictionary key (dict["missing_key"])
ValueError	        > Incorrect value format (int("hello"))
AttributeError	    > Calling an undefined attribute (NoneType object has no attribute .upper())
ImportError	        > Failure to import a module (import nonexistent_module)
FileNotFoundError	> Trying to open a missing file (open("nonexistent.txt"))

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

    # except:
    #     print("Some error occurred")
    
    except Exception as e: #More precise
        print("Some error occurred", e)

    except ValueError:
        print("Please don't perform bad typecast!")
        
    except ZeroDivisionError:
        print("Please don't divide by zero!")
        

    
    
