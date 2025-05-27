# if condition1:
#     # Runs if condition1 is True
# elif condition2:
#     # Runs if condition1 is False and condition2 is True
# else:
#     # Runs if both condition1 and condition2 are False


a = int(input("Please enter your age : "))

if a > 18:
    print("You can drive car!")
elif a == 18:
    print("You need to apply for verification on link> www.checker.com")
else:
    print("You cannot drive!")
    
print("End of program")
