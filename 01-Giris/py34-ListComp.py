numbers=[]

for x in range(10):
    numbers.append(x)
print(numbers)

numbers = [x for x in range(10)]
print(numbers)

# x in karesini alma
numbers = [x**2 for x in range(10)]
print(numbers)

# üçe bölünebilen x değerlerinin karesini alma
numbers = [x**2 for x in range(10) if x % 3 == 0]
print(numbers)

years = [1985,2004,1994,2007,1999,2000]
ages = [2021-year for year in years]
print(ages)

cordinate = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            if x==y and x==z:
                cordinate.append((x,y,z))
print(cordinate)
