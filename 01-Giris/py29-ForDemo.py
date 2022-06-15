sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# Üçün katı olan sayılar hangisidir?
for i in sayilar:
    if i % 3 == 0:
        print(i, end=" ")

# sayılar listesinin toplamı kaçtır
sum = 0
for i in sayilar:
    sum += i
print()
print("Toplam = {0}\n".format(sum))

# sayılar listesindeki tek sayıların karesini alınız.
for i in sayilar:
    if i % 2 == 1:
        print("{0}*{0}={1}".format(i, i*i), end=" ")


sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]
# sehirlerden hangileri en fazla 5 karekterlidir
print(end="\n")
for sehir in sehirler:
    if (len(sehir) < 6):
        print(sehir)

urunler = [
    {"name": "Samsung S6", "price": "3000"},
    {"name": "Samsung S7", "price": "4000"},
    {"name": "Samsung S8", "price": "5000"},
    {"name": "Samsung S9", "price": "6000"},
    {"name": "Samsung S10", "price": "7000"},
]
# ürünlerin toplam fiyatı nedir?
toplamFiyat = 0
for urun in urunler:
    toplamFiyat += int(urun["price"])
    print(urun["price"])
print("Toplam Fiyat = {0}".format(toplamFiyat))

# 5000 den ucuz olan telefonlar
for urun in urunler:
    if int(urun["price"]) <=5000:
        print(urun["name"]," : ",urun[ "price"])