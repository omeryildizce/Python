# 1-100 arası sayıyı bulma oyunu

import random


sayi = random.randint(1,101)

for i in range(5):
    tahmin = int(input("Kalan tahmin Hakkı :{0}\n{1}. Tahmininiz:\n".format(5-i,i+1)))
    if sayi == tahmin:
        print("{0} : Doğru Bildiniz.".format(sayi))
        break
    elif sayi<tahmin:
        print("Daha küçük")
    else:
        print("Daha büyük")
print(sayi)