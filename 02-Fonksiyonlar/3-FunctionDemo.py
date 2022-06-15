import random

#3. Girilen aralıktaki asl sayıları bulma
baslangic = random.randint(2,100)
bitis = random.randint(100,200)
print(baslangic," ",bitis)
def asal(bas,bit):
    listAsal = []
    asalmi = 0
    for i in range(bas,bit+1):
        for j in range (2,i+1):
            if i % j == 0:
                asalmi += 1
        if asalmi == 1:
            listAsal.append(j)
        asalmi=0

    print(listAsal)

asal(baslangic,bitis)


#2. sınırsız sayıda parametreyi listeye ceviren fonksiyon

def listele(*args):
    liste = []

    for i in args:
        liste.append(i)
    print(liste)
    return liste

sayi = random.randint(0,100)
dizi = []
for i in range(0,sayi):
   dizi.append( listele(i))
print(dizi)

#1. gönderilen kelimeyi belirli bir sayıda ekraa yazdırma
def yaz(kelime, tekrar):
    for i in range(tekrar):
        print(kelime)

yaz("Ömer",5)

#4. sayının tam bölenlerini bulma

def bolen(sayi):
    liste=[]

    for i in range(1,sayi+1):
        if sayi % i == 0:
            liste.append(i)
    return liste

print(bolen(20))
