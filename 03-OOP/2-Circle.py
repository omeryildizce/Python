class Circle:
    # class object attribute
    pi = 3.1415

    def __init__(self, yaricap=1):
         self.yaricap = yaricap

    # methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * self.yaricap * self.yaricap

c1 = Circle()
c2 = Circle(5) 

print(f"c1 : alan = {c1.alan_hesapla()}\nc1 : cevre = {c1.cevre_hesapla()}")
print(f"c2 : alan = {c2.alan_hesapla()}\nc2 : cevre = {c2.cevre_hesapla()}")
