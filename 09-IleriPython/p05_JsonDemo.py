import json
import os
yol = "9-IleriPython//p05_users.json"
class User:
    def __init__(self, username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self) :
        self.users=[] 
        self.isLoggedIn = False
        self.currentUSer= {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists(yol):
            with open(yol,"r",encoding="utf-8")as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser) 
            print(self.users)

    def register(self,user: User):
        self.users.append(user)
        self.saveToFile() 
        print("Kullanıcı Oluşturuldu")

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUSer = user
                print("Login yapıldı")
                break
        def logout(self):
             self.isLoggedIn = False
             self.currentUSer={}
             print("çıkış yapıldı")
    def identity(self):
        if self.isLoggedIn:
            print(f"Username: {self.currentUSer.username}")
        else:
            print("Giriş yapılmadı")
    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
      
        with open(yol,"w",encoding="utf-8")as file:
            json.dump(list,file )

secRegister = "1-Register\n"
secLogin = "2-Login\n"
secLogout = "3-Logout\n"
secId = "4-Identity\n"
sec = "5-Exit\nSeçiniz : "

repository = UserRepository()
while True:
    print("Menü".center(50,"*"))
    secim = input(f"{secRegister}{secLogin}{secLogout}{secId}{sec}")

    if secim == "5":
        break
    else:
        if secim=="1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")

            user = User(username=username,password=password,email=email)
            repository.register(user)


        elif secim=="2":
            username = input("Username: ")
            password = input("Password: ")

            repository.login(username,password)
        elif secim=="3":
            repository.logout()
        elif secim == "4":
            repository.identity()
        else:
            print("Hatalı seçim yaptınız.\n")

