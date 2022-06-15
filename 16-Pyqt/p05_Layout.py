import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from  PyQt5.QtGui import  QPalette,QColor
import h11

class Color(QWidget):
    def __init__(self, color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,500,500)

        #2
        # hlayout1 = QtWidgets.QHBoxLayout()
        # hlayout1.addWidget(Color("red"))
        # hlayout1.addWidget(Color("green"))
        # hlayout1.addWidget(Color("blue"))
        # hlayout1.setContentsMargins(50,20,0,0)
        # hlayout1.setSpacig(50)
         
        # hlayout2 = QtWidgets.QHBoxLayout()
        # hlayout2.addWidget(Color("orange"))
        # hlayout2.addWidget(Color("yellow"))
        

        # hlayout3 = QtWidgets.QHBoxLayout()
        # hlayout3.addWidget(Color("aqua"))

        # vlayout = QtWidgets.QVBoxLayout()
        # vlayout.addLayout(hlayout1)
        # vlayout.addLayout(hlayout2)
        # vlayout.addLayout(hlayout3)

        #1
        # layout = QtWidgets.QHBoxLayout()
        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("yellow"))
        # layout.addWidget(Color("aqua"))
        # layout.addWidget(Color("purple"))

        layout = QtWidgets.QGridLayout()
        layout.addWidget(Color("red"),0,0)
        layout.addWidget(Color("blue"),1,0)
        layout.addWidget(Color("green"),2,0)
        layout.addWidget(Color("yellow"),1,1)
        layout.addWidget(Color("aqua"),0,3)
        layout.addWidget(Color("purple"),1,3)
        layout.addWidget(Color("brown"),2,3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()