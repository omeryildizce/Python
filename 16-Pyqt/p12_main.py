import sys
from PyQt5 import QtWidgets
from p12_table import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()  
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(),item.column(),item.text())

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0,QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1,QTableWidgetItem(price))
            

    def loadProducts(self):
        products = [
            {"name":"samsung s5", "price":2000},
            {"name":"samsung s6", "price":3000},
            {"name":"samsung s7", "price":4000},
            {"name":"samsung 75", "price":8000},

        ]

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        rowIndex=0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0,QTableWidgetItem(product["name"]))
            self.ui.tableProducts.setItem(rowIndex,1,QTableWidgetItem(str(product["price"])))
            
            rowIndex +=1
def app():
    app=QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()