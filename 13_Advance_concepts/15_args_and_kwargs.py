# We can use args and kwargs together with one single condition > args should come before kwargs

def fun1(*args,**kwargs):
    print(f"This all are args : {args}")
    print(f"This all are args : {kwargs}")
    
    
fun1(3,1,5,9,"akka", Name= "issmile", age = 23, location = "Nanded")

'''
Output :
This all are args : (3, 1, 5, 9, 'akka')
This all are args : {'Name': 'issmile', 'age': 23, 'location': 'Nanded'}
'''
