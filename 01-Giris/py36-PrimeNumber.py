# Asal sayı 

asal= []
kontrol = 0
number = int(input("Sayı : "))
if number >=2:
    for i in range(2, number+1):
        for j in range(2,i+1):
            if i%j == 0:
                kontrol += 1
        if kontrol == 1:
            asal.append(j)
        
        kontrol= 0

print(asal)

