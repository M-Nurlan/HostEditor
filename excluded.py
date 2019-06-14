from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import *
import sys
from exclude import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
# UIClass, QtBaseClass = uic.loadUiType("excluded.ui")

class Excluded(QtWidgets.QMainWindow):
    includes = pyqtSignal(list)
    global HOST
    HOST = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    def __init__(self, excludeds):
        super(Excluded, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI1()

        self.ui.includeBtn.accepted.connect(self.remove)
        self.ui.includeBtn.rejected.connect(self.hide)
        excludeds[list].connect(self.initUI1)

    def initUI1(self):
        self.setWindowTitle('Excluded')
        self.setFixedSize(505, 268)
        f = open(HOST)
        lines = []
        for line in f:
            if len(line) == 1 and line.find('\n') != -1:
                continue
            elif line.find('\n') == -1:
                line += '\n'
            if line.startswith('#HE '):
                lines.append(line.strip('#HE '))

        self.ui.excludeBrowse.clear()
        self.ui.excludeBrowse.setSelectionMode(QListWidget.ExtendedSelection)
        self.ui.excludeBrowse.addItems(lines)
        self.ui.excludeBrowse.scrollToBottom()
        self.ui.excludeBrowse.show()

    def remove(self):
        listItems = self.ui.excludeBrowse.selectedItems()
        sendingValue = []
        for item in listItems:
            with open(HOST, 'r') as f:
                excludeds = f.readlines()
            with open(HOST, 'w') as f:
                for line in excludeds:
                    if line.strip('\n').strip('#HE ') == item.text().strip('\n').strip('#HE '):
                        f.write(line.strip('#HE '))
                    else:
                        f.write(line)
            sendingValue.append(item.text())
            self.ui.excludeBrowse.takeItem(self.ui.excludeBrowse.row(item))
        self.includes.emit(sendingValue)
        self.hide()
