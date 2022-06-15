import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,450,300)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1 : ")
        self.lbl_sayi1.move(50,40)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,40)
        self.txt_sayi1.resize(200,30)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2 : ")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,30)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,120)
        self.btn_topla.resize(95,30)
        self.btn_topla.clicked.connect(self.hesapla)
                
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(255,120)
        self.btn_cikar.resize(95,30)
        self.btn_cikar.clicked.connect(self.hesapla)

        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText("Çarp")
        self.btn_carpma.move(150,160)
        self.btn_carpma.resize(95,30)
        self.btn_carpma.clicked.connect(self.hesapla)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText("Böl")
        self.btn_bolme.move(255,160)
        self.btn_bolme.resize(95,30)
        self.btn_bolme.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.move(150,200)
        self.lbl_sonuc.resize(200,35)
        self.lbl_sonuc.setText("Sonuç:")
        
    def hesapla(self):
        sender = self.sender().text()
        #print(sender.text())
        result = 0

        sayi1 = int(self.txt_sayi1.text())
        sayi2 = int(self.txt_sayi2.text())

        if sender =="Topla":
            result=sayi1+sayi2
        elif sender == "Çıkar":
             result=sayi1-sayi2
        elif sender == "Çarp":
             result=sayi1*sayi2
        elif sender == "Böl":
            result=sayi1/sayi2
        else:
            self.lbl_sonuc.setText("Hatalı değerler girdiniz")

        
        self.lbl_sonuc.setText("Sonuç : "+ str(result))
     
    # def cikarma(self):
    #     result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("Sonuç : "+str(result))

    # def carp(self):
    #     result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("Sonuç : "+str(result))

    # def bol(self):
    #     result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("Sonuç : "+str(result))


def App():
    app = QApplication(sys.argv)
    win= MainForm()
    win.show()
    sys.exit(app.exec_())



App()