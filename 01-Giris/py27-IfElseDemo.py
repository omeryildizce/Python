# verilen tarihe göre araç yıl bakımı hesaplama
import  datetime
tarih = input("Aracınızın trafiğe çıkış tarihi: (gün/ay/yil):")
tarih = tarih.split("/")

cikisTarihi = datetime.datetime(int(tarih[2]),int(tarih[1]),int(tarih[0]))
simdi = datetime.datetime.now()
fark= simdi - cikisTarihi
days = fark.days
if  days >0 and days<=365:
    print("Bakım Yılı 1")
elif  days >365 and days<=365*2:
    print("Bakım Yılı 2")
elif  days >365*2 and days<=365*3:
    print("Bakım Yılı 3")
else:
    print("hatalı giriş")

# vize final notu ile dersin harf notu ve ortalamasını hesaplayın
vizeKatsayisi = 0.3
finalKatsayisi = 0.8

vize = int(input("Vize Notunuz : "))
final = int(input("Final Notunuz : "))

ortalama = vize * vizeKatsayisi + final*finalKatsayisi
if ortalama<=110 and ortalama>0:
    if ortalama>89:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"A"))
    elif ortalama>84:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"B1"))
    elif ortalama>79:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"B2"))
    elif ortalama>74:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"B3"))
    elif ortalama>69:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"C1"))
    elif ortalama>64:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"C2"))
    elif ortalama>59:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"C3"))
    elif ortalama>49:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"F1"))
    else:
        print("Ortalama : {0}\nHarf notu : {1}".format(ortalama,"F2"))
else:
    print("Ortalama : {0}\nHarf notu : {1}".format(0,"Sınava Girmedi"))





# ehliyet alabilme durumu kontrol: yas >17, ad, eğitim durumu(lise,üniversite)

firstname = input("adınız : ")
surname = input("Soyadınız : ")
age = int(input("Yaşınız : "))
egitim = int(input("Lise için 1'e basınız.Üniversite için 2'ye basınız"))

if age > 17:
    if egitim==1:
        print("Ehliyet alamazsınız.")
    elif egitim==2:
        print("ehliyet alabilirsiniz.")
    else:
        print("hatalı değer girdiniz")
else:
    print("Yaşınız 18 den büyük olmalı")






