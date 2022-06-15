# x= input("1. Sayı : ")
# y =input("2. Sayı : ")

# print(type(x)) # x string veri tipinde

# toplam =int(x)+int(y)
# print(toplam)

""" 
    ctrl k+c, ctrl k+u
"""
from unicodedata import name


x=5 # x is int
y = 10.5 # y is float

name="Ömer" # name is string 
isOnline = True # isOnline is boolean

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))


#int to float
print("*************")
x = float(x)
print(x)
print(type(x))


#float to int
print("*************")
y = int(y)
print(y)
print(type(y))

result = x+y
print("sum: ",result)


#bool to string
print("*************")
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))


#bool to int
print("*************")
isOnline= int(isOnline)
print(isOnline)
print(type(isOnline))












