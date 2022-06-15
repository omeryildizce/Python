# girilen iki sayıdan hangisi büyüktür ?

from unittest import result


sayi1 = int(input("Sayı Giriniz : "))
sayi2 = int(input("Sayı Giriniz : "))

result = sayi1 > sayi2
print(f"Sayı 1:{sayi1} Sayı 2:{sayi2} den büyükmüdür ? {result}")

# sınav ortalamsını hesaplayınız. not >= 60 : Geçti.

vize = int(input("Vize Notunuzu Giriniz : "))
final = int(input("Final Notunuzu Giriniz : "))

result = vize * 0.3 + final * 0.8

if (result >=60):
    print("Geçti : {0}".format(result) )

