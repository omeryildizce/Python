#class
list = [1,2,3,4,5,6,7,8,9,10]
print(type(list)) # class list

class Person:
    #class attributes
    address = "no information"
    #constructor(yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print("__init__ metodu çalıştı")
    
    #instance methods
    def intro(self):
        print("Hello There. I am "+ self.name)
    
    def calculateAge(self):
        return 2022 - self.year

#instance (object)  
p1 = Person("Ali", year = 1990)
p2 = Person( "Veli", 1999)

#update
p1.name= "Ömer"
p1.address= "Malatya"

print(f"p1: name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"p2: name: {p2.name} year: {p2.year}  address: {p2.address}")

p1.intro()
p2.intro()
 
print(p1.calculateAge())

