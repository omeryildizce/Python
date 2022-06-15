# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük değer alamaZ.")

def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("Parola en az 8 karakterli olmalı")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harrf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harrf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$]",psw):
        raise Exception("parola alpha numeric karakter içermelidir.")
    elif  re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")


while True:
    try:
        x = "AAaa__44" #input("Parola: ")
        check_password(x)
        print("***************")
    except Exception as ex:
        print(ex)
    else:
        break
    finally:
        print("Kontrol tamamlandı.")

class Persona:
    def __init__(self,name= "ali",year=1994) :
        if len(name) >10:
            raise Exception("isim 10 karakterden fazla olamaz")
        else:
            self.name = name
            self.year = year
try:
    p = Persona("aliiiiiiiiiiiiii",1856)
except Exception as ex:
    print(ex)