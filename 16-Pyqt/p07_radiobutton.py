# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p07_radiobutton.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxUlke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUlke.setGeometry(QtCore.QRect(10, 10, 180, 270))
        self.groupBoxUlke.setObjectName("groupBoxUlke")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxUlke)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 151, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutUlke = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutUlke.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutUlke.setObjectName("gridLayoutUlke")
        self.radioTurkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioTurkiye.setObjectName("radioTurkiye")
        self.gridLayoutUlke.addWidget(self.radioTurkiye, 0, 0, 1, 1)
        self.radioAzerbaycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAzerbaycan.setObjectName("radioAzerbaycan")
        self.gridLayoutUlke.addWidget(self.radioAzerbaycan, 1, 0, 1, 1)
        self.radioAlmanya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAlmanya.setObjectName("radioAlmanya")
        self.gridLayoutUlke.addWidget(self.radioAlmanya, 2, 0, 1, 1)
        self.radioYunanistan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioYunanistan.setObjectName("radioYunanistan")
        self.gridLayoutUlke.addWidget(self.radioYunanistan, 3, 0, 1, 1)
        self.groupBoxEgitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEgitim.setGeometry(QtCore.QRect(200, 10, 180, 270))
        self.groupBoxEgitim.setObjectName("groupBoxEgitim")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxEgitim)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 151, 231))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutEgitim = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutEgitim.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutEgitim.setObjectName("gridLayoutEgitim")
        self.radioLise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioLise.setObjectName("radioLise")
        self.gridLayoutEgitim.addWidget(self.radioLise, 1, 0, 1, 1)
        self.radioIlkokul = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioIlkokul.setObjectName("radioIlkokul")
        self.gridLayoutEgitim.addWidget(self.radioIlkokul, 0, 0, 1, 1)
        self.radioUniversite = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioUniversite.setObjectName("radioUniversite")
        self.gridLayoutEgitim.addWidget(self.radioUniversite, 2, 0, 1, 1)
        self.radioYuksekLisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioYuksekLisans.setObjectName("radioYuksekLisans")
        self.gridLayoutEgitim.addWidget(self.radioYuksekLisans, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(400, 40, 301, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblUlke = QtWidgets.QLabel(self.widget)
        self.lblUlke.setText("")
        self.lblUlke.setObjectName("lblUlke")
        self.horizontalLayout.addWidget(self.lblUlke)
        self.labelMezun = QtWidgets.QLabel(self.widget)
        self.labelMezun.setText("")
        self.labelMezun.setObjectName("labelMezun")
        self.horizontalLayout.addWidget(self.labelMezun)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(400, 120, 301, 91))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnUlke = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUlke.sizePolicy().hasHeightForWidth())
        self.btnUlke.setSizePolicy(sizePolicy)
        self.btnUlke.setObjectName("btnUlke")
        self.horizontalLayout_2.addWidget(self.btnUlke)
        self.btnEgitim = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEgitim.sizePolicy().hasHeightForWidth())
        self.btnEgitim.setSizePolicy(sizePolicy)
        self.btnEgitim.setObjectName("btnEgitim")
        self.horizontalLayout_2.addWidget(self.btnEgitim)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxUlke.setTitle(_translate("MainWindow", "Ülke"))
        self.radioTurkiye.setText(_translate("MainWindow", "Türkiye"))
        self.radioAzerbaycan.setText(_translate("MainWindow", "Azerbeycan"))
        self.radioAlmanya.setText(_translate("MainWindow", "Almanya"))
        self.radioYunanistan.setText(_translate("MainWindow", "Yunanistan"))
        self.groupBoxEgitim.setTitle(_translate("MainWindow", "Eğitim"))
        self.radioLise.setText(_translate("MainWindow", "Lise"))
        self.radioIlkokul.setText(_translate("MainWindow", "İlkokul"))
        self.radioUniversite.setText(_translate("MainWindow", "Üniversite"))
        self.radioYuksekLisans.setText(_translate("MainWindow", "Yüksek Lisans"))
        self.btnUlke.setText(_translate("MainWindow", "Ülke Seçimi"))
        self.btnEgitim.setText(_translate("MainWindow", "Eğitimi Seçimi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
