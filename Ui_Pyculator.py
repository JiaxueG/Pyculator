# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JIAXUE GONG\Documents\GitHub\Pyculator\Pyculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(597, 480)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setWindowTitle("Pyculator")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 100))
        self.lcdNumber.setDigitCount(12)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.PBTNhisclear = QtWidgets.QPushButton(self.centralwidget)
        self.PBTNhisclear.setObjectName("PBTNhisclear")
        self.verticalLayout_3.addWidget(self.PBTNhisclear)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PBTNcalculate = QtWidgets.QPushButton(self.groupBox)
        self.PBTNcalculate.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PBTNcalculate.setFont(font)
        self.PBTNcalculate.setObjectName("PBTNcalculate")
        self.verticalLayout.addWidget(self.PBTNcalculate)
        self.PBTNclear = QtWidgets.QPushButton(self.groupBox)
        self.PBTNclear.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PBTNclear.setFont(font)
        self.PBTNclear.setObjectName("PBTNclear")
        self.verticalLayout.addWidget(self.PBTNclear)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.PBTNhisclear.setText(_translate("MainWindow", "Clear History"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.PBTNcalculate.setText(_translate("MainWindow", "Calculate"))
        self.PBTNclear.setText(_translate("MainWindow", "Clear"))

