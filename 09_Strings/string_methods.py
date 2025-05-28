name = "KakaKeshav" #strings are immutable

# name[0] = "r"

# print(name)

a= len(name)
print(a)

print(name.upper(), name)
print(name.lower(), name)
print(name.capitalize(), name)

#strip
s = " hello world "
print(s.strip())
print(s.lstrip())
print(s.rstrip)

#find and replace

fr = "Python is fun is awesome is fast"
print(fr.find("n")) # index of first occurence of the string

print(fr.replace("is", "was")) # replaces all the instance of the string given with the string which would replace

# Split

split = "Apples, Bananas, Chickoo"

print(split.split(",")) # creates a list of the elements present in the string with the separation mentioned in the function

#checking string properties >>> returns BOOLEAN output

prop = "HelloNoob"
print(prop.isalpha()) #Op : true>>>>>>>>all alpha bets
print(prop.isdigit()) #Op : false>>>>>all digits
print(prop.isalnum()) #Op : true >>>>Alpanumeric
print(prop.isspace()) #Op : false >>> all space


