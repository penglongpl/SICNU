# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 640)
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.MainLayout = QtWidgets.QHBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.img_MainLayout = QtWidgets.QHBoxLayout()
        self.img_MainLayout.setObjectName("img_MainLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.text_Prev = QtWidgets.QLabel(self.centralwidget)
        self.text_Prev.setAlignment(QtCore.Qt.AlignCenter)
        self.text_Prev.setObjectName("text_Prev")
        self.gridLayout.addWidget(self.text_Prev, 0, 1, 1, 1)
        self.text_Origin = QtWidgets.QLabel(self.centralwidget)
        self.text_Origin.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.text_Origin.setAlignment(QtCore.Qt.AlignCenter)
        self.text_Origin.setObjectName("text_Origin")
        self.gridLayout.addWidget(self.text_Origin, 0, 0, 1, 1)
        self.slider_origin = QtWidgets.QSlider(self.centralwidget)
        self.slider_origin.setOrientation(QtCore.Qt.Horizontal)
        self.slider_origin.setObjectName("slider_origin")
        self.gridLayout.addWidget(self.slider_origin, 2, 0, 1, 1)
        self.scrollArea_prev = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_prev.setWidgetResizable(True)
        self.scrollArea_prev.setObjectName("scrollArea_prev")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 387, 412))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img_prev = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.img_prev.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.img_prev.setAlignment(QtCore.Qt.AlignCenter)
        self.img_prev.setObjectName("img_prev")
        self.verticalLayout_3.addWidget(self.img_prev)
        self.scrollArea_prev.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_prev, 1, 1, 1, 1)
        self.scrollArea_origin = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_origin.setWidgetResizable(True)
        self.scrollArea_origin.setObjectName("scrollArea_origin")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 387, 412))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_origin = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.img_origin.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.img_origin.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.img_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.img_origin.setObjectName("img_origin")
        self.horizontalLayout_2.addWidget(self.img_origin)
        self.scrollArea_origin.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea_origin, 1, 0, 1, 1)
        self.slider_prev = QtWidgets.QSlider(self.centralwidget)
        self.slider_prev.setOrientation(QtCore.Qt.Horizontal)
        self.slider_prev.setObjectName("slider_prev")
        self.gridLayout.addWidget(self.slider_prev, 2, 1, 1, 1)
        self.menu_MainLayout = QtWidgets.QGridLayout()
        self.menu_MainLayout.setObjectName("menu_MainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_open = QtWidgets.QPushButton(self.centralwidget)
        self.button_open.setStyleSheet("")
        self.button_open.setObjectName("button_open")
        self.horizontalLayout.addWidget(self.button_open)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.menu_MainLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setObjectName("button_1")
        self.verticalLayout.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setObjectName("button_2")
        self.verticalLayout.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setObjectName("button_3")
        self.verticalLayout.addWidget(self.button_3)
        self.jhbh_widget = QtWidgets.QWidget(self.centralwidget)
        self.jhbh_widget.setObjectName("jhbh_widget")
        self.jhbh_layout = QtWidgets.QVBoxLayout(self.jhbh_widget)
        self.jhbh_layout.setObjectName("jhbh_layout")
        self.pushButton_PY = QtWidgets.QPushButton(self.jhbh_widget)
        self.pushButton_PY.setObjectName("pushButton_PY")
        self.jhbh_layout.addWidget(self.pushButton_PY)
        self.pushButton_JX = QtWidgets.QPushButton(self.jhbh_widget)
        self.pushButton_JX.setObjectName("pushButton_JX")
        self.jhbh_layout.addWidget(self.pushButton_JX)
        self.pushButton_XZ = QtWidgets.QPushButton(self.jhbh_widget)
        self.pushButton_XZ.setObjectName("pushButton_XZ")
        self.jhbh_layout.addWidget(self.pushButton_XZ)
        self.pushButton_SF = QtWidgets.QPushButton(self.jhbh_widget)
        self.pushButton_SF.setObjectName("pushButton_SF")
        self.jhbh_layout.addWidget(self.pushButton_SF)
        self.pushButton_BX = QtWidgets.QPushButton(self.jhbh_widget)
        self.pushButton_BX.setObjectName("pushButton_BX")
        self.jhbh_layout.addWidget(self.pushButton_BX)
        self.verticalLayout.addWidget(self.jhbh_widget)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setObjectName("button_4")
        self.verticalLayout.addWidget(self.button_4)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setObjectName("button_5")
        self.verticalLayout.addWidget(self.button_5)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setObjectName("button_6")
        self.verticalLayout.addWidget(self.button_6)
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setObjectName("button_7")
        self.verticalLayout.addWidget(self.button_7)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setObjectName("button_8")
        self.verticalLayout.addWidget(self.button_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.menu_MainLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.menu_MainLayout.setRowStretch(0, 2)
        self.gridLayout.addLayout(self.menu_MainLayout, 1, 2, 1, 1)
        self.img_MainLayout.addLayout(self.gridLayout)
        self.MainLayout.addLayout(self.img_MainLayout)
        self.verticalLayout_2.addLayout(self.MainLayout)
        self.widget_PY = QtWidgets.QWidget(self.centralwidget)
        self.widget_PY.setObjectName("widget_PY")
        self.layout_PY = QtWidgets.QHBoxLayout(self.widget_PY)
        self.layout_PY.setObjectName("layout_PY")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setObjectName("formLayout")
        self.slider_PY_V = QtWidgets.QSlider(self.widget_PY)
        self.slider_PY_V.setOrientation(QtCore.Qt.Horizontal)
        self.slider_PY_V.setObjectName("slider_PY_V")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.slider_PY_V)
        self.slider_PY_S = QtWidgets.QSlider(self.widget_PY)
        self.slider_PY_S.setOrientation(QtCore.Qt.Horizontal)
        self.slider_PY_S.setObjectName("slider_PY_S")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.slider_PY_S)
        self.label_V = QtWidgets.QLabel(self.widget_PY)
        self.label_V.setObjectName("label_V")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_V)
        self.label_S = QtWidgets.QLabel(self.widget_PY)
        self.label_S.setObjectName("label_S")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_S)
        self.layout_PY.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_PY.addItem(spacerItem2)
        self.layout_PY.setStretch(1, 3)
        self.verticalLayout_2.addWidget(self.widget_PY)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 23))
        self.menubar.setObjectName("menubar")
        self.menuwenjian = QtWidgets.QMenu(self.menubar)
        self.menuwenjian.setObjectName("menuwenjian")
        self.title_about = QtWidgets.QMenu(self.menubar)
        self.title_about.setObjectName("title_about")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioninfo = QtWidgets.QAction(MainWindow)
        self.actioninfo.setObjectName("actioninfo")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.menuwenjian.addAction(self.action_open)
        self.menuwenjian.addAction(self.action_save)
        self.menuwenjian.addAction(self.action_quit)
        self.title_about.addAction(self.action_about)
        self.menubar.addAction(self.menuwenjian.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.title_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理-wjsaya.top"))
        self.text_Prev.setText(_translate("MainWindow", "效果图"))
        self.text_Origin.setText(_translate("MainWindow", "原图"))
        self.img_prev.setText(_translate("MainWindow", "预览图展示区"))
        self.img_origin.setText(_translate("MainWindow", "原图展示区"))
        self.button_open.setText(_translate("MainWindow", "打开(ctrl+o)"))
        self.button_save.setText(_translate("MainWindow", "保存(ctrl+s)"))
        self.button_1.setText(_translate("MainWindow", "彩色->灰度"))
        self.button_2.setText(_translate("MainWindow", "灰度->二值"))
        self.button_3.setText(_translate("MainWindow", "几何变换"))
        self.pushButton_PY.setText(_translate("MainWindow", "平移"))
        self.pushButton_JX.setText(_translate("MainWindow", "镜像"))
        self.pushButton_XZ.setText(_translate("MainWindow", "旋转"))
        self.pushButton_SF.setText(_translate("MainWindow", "缩放"))
        self.pushButton_BX.setText(_translate("MainWindow", "变形"))
        self.button_4.setText(_translate("MainWindow", "去噪"))
        self.button_5.setText(_translate("MainWindow", "PushButton"))
        self.button_6.setText(_translate("MainWindow", "边缘提取(一阶差分)"))
        self.button_7.setText(_translate("MainWindow", "加噪"))
        self.button_8.setText(_translate("MainWindow", "退出(ctrl+q)"))
        self.label_V.setText(_translate("MainWindow", "水平"))
        self.label_S.setText(_translate("MainWindow", "垂直"))
        self.menuwenjian.setTitle(_translate("MainWindow", "文件"))
        self.title_about.setTitle(_translate("MainWindow", "关于"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.actioninfo.setText(_translate("MainWindow", "info"))
        self.action_about.setText(_translate("MainWindow", "关于我们"))
        self.action_quit.setText(_translate("MainWindow", "退出(ctrl+q)"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_open.setText(_translate("MainWindow", "打开(ctrl+o)"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "保存(ctrl+s)"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))

