# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pu1 = QtWidgets.QPushButton(self.centralwidget)
        self.pu1.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.pu1.setObjectName("pu1")
        self.wi1 = QtWidgets.QWidget(self.centralwidget)
        self.wi1.setGeometry(QtCore.QRect(210, 390, 160, 80))
        self.wi1.setObjectName("wi1")
        self.lay1 = QtWidgets.QVBoxLayout(self.wi1)
        self.lay1.setContentsMargins(0, 0, 0, 0)
        self.lay1.setObjectName("lay1")
        self.pushButton_2 = QtWidgets.QPushButton(self.wi1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lay1.addWidget(self.pushButton_2)
        self.groupBox = QtWidgets.QGroupBox(self.wi1)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 30, 54, 12))
        self.label.setObjectName("label")
        self.lay1.addWidget(self.groupBox)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(300, 220, 160, 83))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.lay2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.lay2.setContentsMargins(0, 0, 0, 0)
        self.lay2.setObjectName("lay2")
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lay2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lay2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lay2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.lay2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lay2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lay2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(400, 320, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pu2 = QtWidgets.QPushButton(self.centralwidget)
        self.pu2.setGeometry(QtCore.QRect(120, 90, 75, 23))
        self.pu2.setObjectName("pu2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.pu1.setText(_translate("MainWindow", "hide"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pu2.setText(_translate("MainWindow", "PushButton"))

