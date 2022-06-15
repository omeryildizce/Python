def changeName(n):
    n = "ada"


name = "ömer"

changeName(name)
print(name)  # name = ömer


def change(n):
    n[0] = "İstanbul"


sehirler = ["Ankara", "İzmir"]

change(sehirler)
print(sehirler)  # istanbul,izmir


def change(n):
    n[0] = "İstanbul"


sehirler = ["Ankara", "İzmir"]

change(sehirler[:])  # [:] verinin kopyasını gönderir
print(sehirler)  # Ankara ,izmir


def add(*params):
    return sum((params))

top = add(10, 20,50,45)
print(top)

def displayUser(**params):
    for key, value in params.items():
        print("{0} is {1}".format(key,value))
    print("")

displayUser(name="Ömer", age=25, city="Ankara")
displayUser(name="Ali", age=15, city="Van", phone="542536")
displayUser(name="Hamdi", age=45, city="Kayseri", phone="585487", emeail="bla@blamail.com")


