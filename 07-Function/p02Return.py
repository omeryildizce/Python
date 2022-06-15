def usalma(number):
    def inner (power):
        return number** power
    return inner

two = usalma(2)
a = two(3)
print(a)


def yetki(page):
    def inner(role):
        if role =="admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
    return inner

user1 = yetki("Product yetki")
print(user1("admin"))
print(user1("user"))


def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+= i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi =="toplam":
        return toplam
    else:
        return carpma
  
yap = islem("toplam")

print(yap(5,45))
