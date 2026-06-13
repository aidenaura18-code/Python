a=[1,2,3]
b=a
print(a is b)

a= [1,2,3]
b= [1,2,3]
print(a is b)
print(a is not b)   

fruits = ["apple", "banana", "cherry"]
print('banana' in fruits)
print("mango " in fruits)
print(' grape ' not in fruits)


a=5
b=3
print(a & b)

a=5 
b=3
print(a | b)


print(5^3)

x=5
if(type(x) is float ):
    print("true")
else:
    print("false")

x=20
y=20
if(x is y):
    print("x & y same identity")

y=30
if(x is not y):
    print("x & y not same identity")   
