#Arithmetic operators

a= 52
b= 4
c= True
d= False

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b) #> Floor division = quotient
print("a % b = ", a % b) #> Modulo = remainder
print("a ** b = ", a ** b)

# Comparison operators : Always return the TRUE or FALSE

print(a>4)
print(a<4)
print(a>=4)
print(a<=4)
print(a==4) #> if equal to not assignment , it's comparing
print(a!=4) #> is a not equal to 4?

#Logical operators >> AND , OR , NOT.

c = True 
d = False

print("AND Operator")
print(c and c)
print(d and c)
print(c and d)
print(d and d)

print("For Or Operator...")
print(c or c)
print(c or d)
print(d or c)
print(d or d)

print("Not Operator")
print(not(c) ) 
print(not(d) ) 


#Assigment operators >> = , += , -= , *= , /= , %= , //= .
f = 10
print(f)
f += 2
print("+= operator>>",f)
f -= 2
print("-= operator>>",f)
f *= 2
print("*= operator>>",f)
f /= 2
print("/= operator>>",f)
f %= 2
print("%= operator>>",f)
f //= 2
print("//= operator>>",f)

#Membership Operators >> in, not in

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) 
print("pineapple" in fruits)

#Identity Operators  >> is, is not

i = 10
j = 11

print("Assignment operator : ",i is j)


