yol ="6-Files//p05NotDemo.txt"
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenci = liste[0]
    notlar = liste[1].split(",")
    ortalama = (int(notlar[0])+int(notlar[1])+int(notlar[2]))/3
    
    if ortalama <=100 and ortalama >=0 :
        if ortalama > 90:
            harf="A"
        elif ortalama > 75:
            harf="B"
        elif ortalama > 60:
            harf="C"
        elif ortalama > 50:
            harf="f1"
        else:
            harf="f2"
    return ogrenci + ":" + harf + "\n"
    
def notlari_kaydet():
    with open(yol,"r+",encoding="utf-8")as file:
        liste =[]

        for i in file:
            liste.append(not_hesapla(i))
        
        with open("6-Files//p05NotSonuc.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

def ortalamalari_oku():
    with open(yol,"r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir), end="")
        print("********************\n")
def not_gir():
    ad = input("Öğrenic Adı : ")
    soyad = input("Öğrenic Soyadı : ")
    not1 = input("Not 1 : ")
    not2 = input("Not 2 : ")
    not3 = input("Not 3 : ")

    with open(yol,"a",encoding="utf-8") as file:
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")


while True:
    islem = input("1-Notları Oku\n2-Not Gir\n3-Notları Kaydet\n4-Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kaydet()
    else:
        break