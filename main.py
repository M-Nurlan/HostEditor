from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from main1 import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from excluded import Excluded
# UIClass, QtBaseClass = uic.loadUiType("main.ui")

class MyApp(QtWidgets.QMainWindow):
    excludeds = pyqtSignal(list)
    global HOST
    HOST = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window = Excluded(self.excludeds)
        self.initUI()
        self.ui.addBtn.clicked.connect(self.addHost)
        self.ui.deleteBtn.clicked.connect(self.deleteHost)
        self.ui.excludeBtn.clicked.connect(self.excludeHost)
        self.ui.removeFromExclude.clicked.connect(self.openExcludeds)
        self.window.includes[list].connect(self.initUI)

    def initUI(self):
        self.setFixedSize(475, 372)
        self.setWindowTitle('Host Reader')
        lines = []
        exists = os.path.isfile('hosts.bak')
        if not exists:
            with open(HOST, 'r') as f:
                backUp = f.readlines()
            for backUpLine in backUp:
                with open('hosts.bak', 'a') as w:
                    w.write(backUpLine)
        with open(HOST, 'r') as hr:
            items = hr.readlines()
        for line in items:
            if len(line) == 1 and line.find('\n') != -1:
                continue
            elif line.startswith('#'):
                continue
            elif line.find('\n') == -1:
                line += '\n'
            lines.append(line)

        self.ui.hostBrowser.clear()
        self.ui.hostBrowser.setSelectionMode(QListWidget.ExtendedSelection)
        self.ui.hostBrowser.addItems(lines)
        self.ui.hostBrowser.scrollToBottom()
        self.ui.hostBrowser.show()
        self.show()

    def openExcludeds(self):
        self.window.show()

    def addHost(self):
        text = self.ui.hostEditor.toPlainText()
        with open(HOST, 'a') as f:
            f.write(text + '\n')
        for line in text.split('\n'):
            self.ui.hostBrowser.addItem(line + '\n')
        self.ui.hostEditor.clear()
        self.ui.hostBrowser.scrollToBottom()
        self.ui.hostBrowser.show()

    def excludeHost(self):
        listItems=self.ui.hostBrowser.selectedItems()
        if not listItems: return
        excludeList = []
        for item in listItems:
            with open(HOST, 'r') as f:
                hostLines = f.readlines()
            with open(HOST, 'w') as f:
                for hostLine in hostLines:
                    if hostLine.strip('\n') == item.text().strip('\n'):
                        f.write('#HE ' + hostLine)
                    else:
                        f.write(hostLine)
            excludeList.append(item.text())
            self.ui.hostBrowser.takeItem(self.ui.hostBrowser.row(item))
        self.excludeds.emit(excludeList)

    def deleteHost(self):
        listItems=self.ui.hostBrowser.selectedItems()
        if not listItems: return
        for item in listItems:
            print(item.text())
            with open(HOST, 'r') as f:
                hostLines = f.readlines()
            with open(HOST, 'w') as f:
                for line in hostLines:
                    if line.strip("\n") != item.text().strip("\n"):
                        f.write(line)
            self.ui.hostBrowser.takeItem(self.ui.hostBrowser.row(item))
        self.ui.hostBrowser.scrollToBottom()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
