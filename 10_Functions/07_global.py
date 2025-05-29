#Using the global keyword
# to modify the a global variable inside a function, use the global keyword

def sum(a,b):
    c = a + b
    print("Hey, I am summing : ")
    global z
    z = 10
    return c

z = 8
print("initial value: ", z)
print(sum(2,8))
print("final value", z)
