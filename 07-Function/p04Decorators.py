def my_decorators(func):
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print("fonksiyondan sonra işlemler")
    return wrapper

def hello():
    print("hello world")


@my_decorators
def greeting():
    print("greeting")


hello = my_decorators(hello)
hello()


greeting()


############################################
import math
import time
from tkinter.messagebox import RETRY
def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(func.__name__," : ",finish-start)
    return inner

@calculate_time
def usalma(a,b):
   
    print(math.pow(a,b))

@calculate_time 
def faktoriyel(a):
    print(math.factorial(a))
   

usalma(2,15)
faktoriyel(10)