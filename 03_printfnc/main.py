print("Hello", 'World', 4)
#observe here that a space character is seen even if we haven't mentioned it while passing the arguments
print("hello")
print("world")
# to avoid this space characther between the arguments we have to override the separation case i.e. space in this context

print("hello", "india", 5, sep=",")

# the default value of sep is " " we have overridden it with "," in this example

# end > The end parameter determines what happens at the end of the printed output. By default it is the new line > \n

print("hello" ,end="-")
print("world")

