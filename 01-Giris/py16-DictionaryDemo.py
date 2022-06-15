ogrenciler = {
    "120":
    {
        "ad" : "Ali",
        "soyad" : "Yılmaz",
        "telefon" : "532 000 00 01"
    } ,
    "125":
    {
        "ad" : "Can",
        "soyad" : "Yılmaz",
        "telefon" : "532 000 00 02"
    } ,
    "128":
    {
        "ad" : "Yılmaz" ,
        "soyad" : "Can",
        "telefon" : "532 000 00 03"
    } 
}

ogrenci = input("Öğrenci Numarası :  ")

print(ogrenciler[ogrenci]["ad"])
print(ogrenciler[ogrenci]["soyad"])
print(ogrenciler[ogrenci]["telefon"])

