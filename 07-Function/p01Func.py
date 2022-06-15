def greeting(name):
    print("Hello", name)

print(greeting("ali"))
print(greeting)

# encapsulation
def outer(num1):
    def inner_increment(num1):
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1,num2)

outer(55)

"""---------------"""

def factorial(number):
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number -1)
    
    return inner_factorial(number)

f = factorial(10)
print(f)