from asyncore import read


yol = "6-Files//p02Reading.txt"

try:
    file = open(yol , "x", encoding="utf-8")
except:
    print()

file = open(yol , "w", encoding="utf-8")
file.write("Ömer\nAli Kadir\nAyşe")
file.close()

print("****************************")
file = open(yol,"r",encoding="utf-8")
for i in file:
    print(i)
file.close()

print("****************************")
file = open(yol,"r",encoding="utf-8")
content = file.read()
print(content)
file.close()

print("****************************")
file = open(yol,"r",encoding="utf-8")
content = file.readline()
print(content)
print(file.readline())
file.close()