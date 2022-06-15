import sys
from PyQt5 import QtWidgets
from p06_checkbox import  Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnSecilenleriAl.clicked.connect(self.getaAllChecked)
        self.ui.btnDersleriAl.clicked.connect(self.dersler)

    def getaAllChecked(self):
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        text=""
        for i in items:
            if i.isChecked():
                text += i.text() + "\n"
        self.ui.lblResult.setText(text)

    def dersler(self):
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
        text=""
        for i in items:
            if i.isChecked():
                text += i.text() + "\n"
        self.ui.lblResultHobiler.setText(text)

    def show_state(self,value):
        cb = self.sender()
        
        print(value)
        print(cb.text())
        print(cb.isChecked())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()