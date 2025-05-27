'''
similar to switch case
newly added in python can be used instead of if else
They provide a powerful way to handle different cases in a more readable and efficient manner, similar to switch statements in other languages.

'''

a = int(input("Enter your lucky number: "))

match a:
    case 4:
        print("you won 4$!!")
    case 7:
        print("Siuuuuuuuuuuuuuuuuuuuu")
    case 8:
        print("7+1 crore!!")
    case _:
        print("Better luck next time, fella.")
        
