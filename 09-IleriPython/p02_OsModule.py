import os
from unittest import result

result =  dir(os)

print(os.name)
print(os.getcwd())


#os.chdir("C://")
#os.chdir("../..")

#os.mkdir("9-IleriPython//yeni klasör") 

print(os.listdir())

print("****************")
for dosya in os.listdir("9-IleriPython"):
    if dosya.endswith(".py"):
        print(dosya)

import datetime
result = os.stat("9-IleriPython//p01_Date.py")
sonuc= result.st_size/1024
print(sonuc)
# oluşturulma
sonuc=  datetime.datetime.fromtimestamp(result.st_ctime)
print(sonuc)
# son erişim
sonuc=  datetime.datetime.fromtimestamp(result.st_atime)
print(sonuc)
# değiştirilme tarihi
sonuc=  datetime.datetime.fromtimestamp(result.st_mtime)
print(sonuc)

os.system("notepad.exe")

