from PyQt5 import QtWidgets
import sys
from p04_MainWindow import Ui_UI_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_UI_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla) 

    def hesapla(self):
        sender = self.sender().text()
        result = 0
        
        sayi1 = int(self.ui.txt_sayi1.text())
        sayi2 = int(self.ui.txt_sayi2.text())

        if sender == "Toplama":
            result = sayi1+sayi2
        elif sender == "Çıkarma":
            result = sayi1-sayi2
        elif sender == "Çarpma":
            result= sayi1*sayi2
        elif sender == "Bölme":
            if sayi2 == 0:
                result=sayi1/1
            else:
                result = sayi1/sayi2
        else:
            self.ui.lbl_sonuc.setText   ("Sonuç : INF")
        
        self.ui.lbl_sonuc.setText("Sonuç : "+str(result))

def App():
    app =  QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

App()