message=" HELLO THERE. My name is Ömer YILDIZ"

print(message)

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())
print(message.strip()) # başlangıçtaki boşluk karakterini siler.
print(message.split()) # boşluğa göre bölme işlemi yapar
print(message.split("."))

# message = " ".join(message)  # split ile ayırdığımızı elemanları birleştirir.

print(message.find("Ömer")) # ilk indexi gösterir
print(message.startswith("H")) # H ilemi başlıyor
print(message.endswith("S"))
print(message.replace(" ","---")) # Boşluk ile 3 çizgiyi değiştirir.

print(message.center(100,"/")) #mesaj 100 karakter olur









