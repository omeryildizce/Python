import sys
from tracemalloc import start
from PyQt5 import QtWidgets
from p10_date import Ui_MainWindow
from PyQt5.QtCore import QDate,QTime,QDateTime

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.Calculate)

    def Calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start,end)

        print("Days in mounth: {0}".format(start.daysInMonth()))
        print("Days in year: {0}".format(start.daysInYear()))

        print("Total Days: {0}".format(start.daysTo(end)))
        now = QDate.currentDate()
        print("Total days from now: {0}".format(start.daysTo(now)))

        print("Days in mounth: {0}".format(start.daysInMonth()))


def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()