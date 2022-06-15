#python -m PyQt5.uic.pyuic -x p06_checkbox.ui  -o p06_checkbox..py
import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon



def window():
    app =QApplication(sys.argv)
    win=QMainWindow()

   
   
    win.setWindowTitle("First App")
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("My tool tip") # uygulama üzerine geldiğinde yazacak yazı

    lbl_name =QtWidgets.QLabel(win)
    lbl_name.setText("Adınız: ")
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız:")
    lbl_surname.move(50,60)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,60)

    def clicked(self):
        print("Butona Tıklandı name: "+txt_name.text()+" surname: "+txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Gönder")
    btn_save.move(150,90)

    (btn_save.clicked.connect(clicked))
 

    win.show()
    sys.exit(app.exec_())
    
window()