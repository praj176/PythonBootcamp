class Point:
    def __init__(self, x, y):
        """Constructor: Initializes the x and y values for a point"""
        self.x = x
        self.y = y
        
    def __add__(self, other):
        """Overloads the + operator to add two Point objects"""
        return Point(self.x + other.x, self.y + other.y)
    
    def sum(self, p):
        """Adds two points and returns a new Point object"""
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_p(self):
        """Displays the x and y values of the point"""
        return f"X is {self.x} and Y is {self.y}"
    
    def __sub__(self, other):
        """Overloads the - operator to subtract two Point objects"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        """Overloads the * operator to multiply the point coordinates by a number"""
        return Point(self.x * factor, self.y * factor)
    
# Creating two points
p1 = Point(4, 1)
p2 = Point(2, 7)

"""
Operator overloading in Python lets us customize how operators (+, -, *, etc.) work for objects. 
We can overload the + operator so that adding two points directly (p1 + p2) works instead of calling sum().


"""
# Adding the two points >> Conventional way
# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2

# Using overloaded + operator instead of sum()
p = p1 + p2  # Addition
p_sub = p1 - p2  # Subtraction
p_mul = p1 * 2   # Multiplication by 2

# Printing the result
print(p.print_p())  # Output: X is 6 and Y is 8
print(p_sub.print_p())  # Output: X is 2 and Y is -6
print(p_mul.print_p())  # Output: X is 8 and Y is 2

