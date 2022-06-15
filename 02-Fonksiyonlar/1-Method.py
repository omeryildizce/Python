# method

list = [1, 2, 3, 4, 5]
list.append(6)  # apend method

# methodlar sınıfın üyesi


# fonksiyon

def merhaba(name="Admin"):
    print("Hello, {0}".format(name))


merhaba("Ömer")
merhaba()


def merhaba1(name="Admin"):
    return "Hello, " + name


selam = merhaba1("Ali")
print(selam)


def sum(number1=0, number2=0):
    return number2 + number1


print(sum(10, 20))

def yasHesapla(yil =2022 ):
    return 2022 - yil

print(yasHesapla(1995))


