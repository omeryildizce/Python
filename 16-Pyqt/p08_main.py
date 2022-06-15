from PyQt5 import QtWidgets
import sys
from p08_combobox import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo =  self.ui.cbSehirler
        combo.addItem(  "Adana")
        combo.addItem("Ankara")
        combo.addItem("Bursa")
        combo.addItem("Kocaeli")
        combo.addItem("İstanbul")
        combo.addItem("İzmir")
        #combo.addItems(["Kastamonu","Niğde","Rize","Trabzon","Van"])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItems)
        self.ui.btnClear.clicked.connect(self.clearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChanged)

    def clearItems(self):
        self.ui.cbSehirler.clear()

    def SelectedIndex(self,index):
        print(index)
    def SelectedChanged(self,text):
        print(text)

    def GetItems(self):
 
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        
        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))
        

    def LoadItems(self):
        sehirler =  ["Kastamonu","Niğde","Rize","Trabzon","Van"]
        self.ui.cbSehirler.addItems(sehirler)

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
