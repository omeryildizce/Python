def square(num): return num**2

result = square(2)
print(result)

numbers = [1,3,5,9,11 ,13,15,10,4,14]
result =list (map(square, numbers))
print(result)

for i in map(square,numbers):
    print(i)

result =list (map(lambda num: num**2, numbers))
print(result)

kare = lambda num: num**2
result =list (map(kare, numbers))
print(result)

print(kare(5))


numbers1 = [1,3,5,9,11 ,13,15,10,4,14]

def even(num): return num%2==0

result = list(filter(even, numbers1))
print(result)

result = list(filter(lambda num: num%2 == 0, numbers1))
print(result)