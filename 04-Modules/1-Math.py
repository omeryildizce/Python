import math 

value = dir(math) # yapabileceğimiz işlemleri gösterir
print(value)

"""
value = help(math)
print(value)
"""

value = help(math.factorial)
print(value)

print(math.factorial(5))
print(math.sqrt(25))
print(math.floor(5.9))
print(math.ceil(5.9))

def ceil(x):
    print("x : " + str(x) )


from math import  * # hepsi  //factorial,sqrt
print(factorial(5))
print(sqrt(45))

print("**************")
print(ceil(5.2)) # son tanımlananı çalıştırır




