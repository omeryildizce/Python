from unicodedata import name


name = ["Ali", "Yağmur", "Hakan" ,"Deniz"]
years = [1998, 2000, 1998, 1987]

name.append("Cenk")
name.insert(0,"Sena")
name.remove("Deniz")
name.append("Deniz")

print(name.index("Deniz"))
print("Ali" in name)

name.reverse()
print(name)
name.reverse()
name.sort()

print(name)
print(years)

yil =int(input("Doğum yılı : ")) 
years.append(yil)

yil =int(input("Doğum yılı : ")) 
years.append(yil)

yil =int(input("Doğum yılı : ")) 
years.append(yil)
print(years)