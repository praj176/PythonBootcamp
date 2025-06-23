import argparse  # Import the argparse module to read command-line arguments

# Step 1: Create the ArgumentParser object
parser = argparse.ArgumentParser(description="Simple command-line calculator")

# Step 2: Add required arguments
parser.add_argument("num1", type=float, help="First number")        # Takes the first number (e.g., 5)
parser.add_argument("operator", type=str, help="Operator (+, -, *, /)")  # Takes the operator (e.g., +)
parser.add_argument("num2", type=float, help="Second number")       # Takes the second number (e.g., 3)

# Step 3: Parse the arguments from the command line
args = parser.parse_args()

# Step 4: Perform the calculation based on the operator
if args.operator == "+":
    result = args.num1 + args.num2
elif args.operator == "-":
    result = args.num1 - args.num2
elif args.operator == "*":
    result = args.num1 * args.num2
elif args.operator == "/":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        result = "Cannot divide by zero"  # Prevents division by 0
else:
    result = "Invalid operator"  # If user gives unsupported operator

# Step 5: Print the result
print("Result:", result)

'''
execution >>>
python calc.py 10 * 5

'''
