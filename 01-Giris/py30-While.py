x = 0

while x <= 100:
    print(x)
    x += 1

x= 0
while x <= 100:
    if x%2 == 0:
       print(x)
    x += 1

name = ""
while  not name.strip(): # boşluk silme
    name = input("İsminiz")
    print(name)
