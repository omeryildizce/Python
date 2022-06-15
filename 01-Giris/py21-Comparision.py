import re


a, b, c, d = 5, 5, 10, 4

result = a == b  # a ile b eşit mi ?
print(result)  # True

result = a == c  # false
print(result)

result = a != b  # a ile b eşit değil mi ?
print(result)  # false

result = a != c  # a ile c eşit değil mi ?
print(result)  # true

result = a < c  # a c'den küçük mü ?
print(result)  # true

result = a > c  # a c'den büyük mü ?
print(result)  # false

result = a <= c  # a küçük eşit c mi ?
print(result)  # true

result = a >= c  # a büyük eşit c mi ?
print(result)  # false


print(False + True + True*5 + 50)  # toplamı 56 dir


username = "Ömer"
password = "12345"

kullanici = username == input("Kullanıcı Adınız : ")
sifre = password == input("Şfreniz : ")

print("Kullanıcı Adınız : {0} \nŞifreniz : {1}".format(kullanici, sifre))
