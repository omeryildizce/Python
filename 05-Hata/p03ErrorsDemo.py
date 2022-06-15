liste = ["1","2","5a","10b","abc","10","50"]

for x in liste:
    try:
       result =  int(x)
       print(result)
    except ValueError:
        print("{0} bir sayı değil.".format(x))


print("------------------------------")

while  True:
    sayi = input("Sayı (q) : ")
    if sayi == "q":
        break
    try:
        result = float(sayi)
    except ValueError:
        print("Geçersiz değer")
    
print("------------------------------")

turkce_karakter = "ıİşŞÇçöÖğĞüÜ"
parola = input("Parola : ")

for i in parola:
    if i in turkce_karakter:
        raise TypeError("Parola türkçe karakter içeremez")
    else:
        pass

