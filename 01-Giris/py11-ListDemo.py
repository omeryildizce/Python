from calendar import calendar


cars = ["Bmw", "Mercedes", "Opel", "Mazda"]

eleman =len(cars)
print(eleman)
print(cars[0])
print(cars[eleman-1])

cars[3] = "Toyota"
print(cars[3])

icerirmi = "Mercedes" in cars
print(icerirmi)

print(cars[-2])

print(cars[:3])

cars[2:] = ["Toyota", "Renault"]
print(cars)

cars += ["Audi", "Nissan"]
print(cars)

del cars[-1]
print(cars)
print(cars[::-1])


studentA = ["Hüseyin", "Şahin", 2016, [65, 45, 75]]
studentB = ["Ömer", "YIDIZ", 2016, [100, 100, 100]]
studentC = ["Ali", "Atay", 2019, [45, 45, 75]]

students = studentA+studentB+studentC
print(students[0:4][:])
