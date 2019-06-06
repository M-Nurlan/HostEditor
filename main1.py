# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 314)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(370, 140, 81, 23))
        self.deleteBtn.setObjectName("deleteBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(370, 230, 81, 23))
        self.addBtn.setAutoDefault(True)
        self.addBtn.setDefault(True)
        self.addBtn.setObjectName("addBtn")
        self.hostBrowser = QtWidgets.QListWidget(self.centralwidget)
        self.hostBrowser.setGeometry(QtCore.QRect(20, 30, 431, 101))
        self.hostBrowser.setObjectName("hostBrowser")
        self.hostEditor = QtWidgets.QLineEdit(self.centralwidget)
        self.hostEditor.setGeometry(QtCore.QRect(20, 200, 431, 20))
        self.hostEditor.setObjectName("hostEditor")
        self.excludeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.excludeBtn.setGeometry(QtCore.QRect(280, 140, 75, 23))
        self.excludeBtn.setObjectName("excludeBtn")
        self.removeFromExclude = QtWidgets.QPushButton(self.centralwidget)
        self.removeFromExclude.setGeometry(QtCore.QRect(20, 140, 101, 23))
        self.removeFromExclude.setObjectName("removeFromExclude")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 51, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 21))
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
        self.deleteBtn.setText(_translate("MainWindow", "Delete"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.hostEditor.setPlaceholderText(_translate("MainWindow", "Write new host..."))
        self.excludeBtn.setText(_translate("MainWindow", "Exclude"))
        self.removeFromExclude.setText(_translate("MainWindow", "Browse excluded"))
        self.label.setText(_translate("MainWindow", "Hosts"))
        self.label_2.setText(_translate("MainWindow", "Add host"))
