from urllib.parse import urlunsplit


sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# sayiları while döngüsü ile ekrana yazdırma
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1


# 100 den 1 e kadar yazdırma
i = 100
while i > 0:
    print(i)
    i -= 1

# kullanıcıdan sözlük verisi alma
urunler = []

adet = int(input("Kaç adet ürün eklemek istiyorsunuz ? \n"))
i = 0
print()
while i < adet:
    name = input("Ürün Adı : ")
    price = input("Fiyatı   : ")
    urunler.append(
        {
            "name": name,
            "price": price
        })
    i += 1
print(urunler)
# kullanıcıdan alınan 5 sayıyı sıralı şekilde yazdırma
numbers = []
i = 0

while i < 5:
    sayi = int(input("{0}. sayı giriniz : ".format(i+1)))
    numbers.append(sayi)
    i += 1
numbers.sort()
print(numbers)

# kullanıcıdan değer aralığını alma
baslangic = int(input("Başlangıç değeri"))
son = int(input("Son değer"))
i = baslangic
while i <= son:
    print(i)
    i += 1
