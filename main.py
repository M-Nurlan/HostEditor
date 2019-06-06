from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import *
import sys
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
        self.setFixedSize(473, 314)
        self.setWindowTitle('Host Reader')
        f = open('src/writehost.txt')
        lines = []
        lineChecker = 0
        with open(HOST, 'r') as hr:
            items = hr.readlines()
        for item in items:
            if item.strip('\n') == "#DO NOT DELETE THIS LINE!!! IT'S USED BY HOST READER!":
                lineChecker = 1
        if lineChecker == 0:
            with open(HOST, 'a') as h:
                h.write("\n" + "#DO NOT DELETE THIS LINE!!! IT'S USED BY HOST READER!" + "\n")

        for line in f:
            if len(line) == 1 and line.find('\n') != -1:
                continue
            elif line.find('\n') == -1:
                line += '\n'
            lines.append(line)

        self.ui.hostBrowser.addItems(lines)
        self.ui.hostBrowser.scrollToBottom()
        self.ui.hostBrowser.show()

        self.show()
        f.close

    def openExcludeds(self):
        # self.window = QtWidgets.QMainWindow()

        # self.ui.setupUi(self.window)
        # self.hide()
        self.window.show()

    def addHost(self):
        f = open('src/writehost.txt', 'a')
        f.write(self.ui.hostEditor.text() + '\n')
        f.close
        f = open(HOST, 'a')
        f.write(self.ui.hostEditor.text() + '\n')
        self.ui.hostBrowser.addItem(self.ui.hostEditor.text() + '\n')
        self.ui.hostEditor.clear()
        self.ui.hostBrowser.scrollToBottom()
        self.ui.hostBrowser.show()
        f.close

    def excludeHost(self):
        f = open('src/excluded.txt', 'a')
        listItems=self.ui.hostBrowser.selectedItems()
        if not listItems: return
        excludeList = []
        for item in listItems:
            with open('src/writehost.txt', 'r') as fread:
                lines = fread.readlines()
            for line in lines:
                if line.strip('\n') == self.ui.hostBrowser.currentItem().text().strip("\n"):
                    f.write(self.ui.hostBrowser.currentItem().text())
            with open("src/writehost.txt", "w") as file:
                for line in lines:
                    if line.strip("\n") != self.ui.hostBrowser.currentItem().text().strip("\n"):
                        file.write(line)
            with open('src/writehost.txt', 'r') as f:
                linesAfterDelete = f.readlines()
            with open(HOST, 'r') as f:
                hostLines = f.readlines()
            with open(HOST, 'w') as f:
                for hostLine in hostLines:
                    f.write(hostLine)
                    if hostLine.strip('\n') == "#DO NOT DELETE THIS LINE!!! IT'S USED BY HOST READER!":
                        f.write('\n'.join(linesAfterDelete))
                        break
            excludeList.append(item.text())
            self.ui.hostBrowser.takeItem(self.ui.hostBrowser.row(item))
        self.excludeds.emit(excludeList)

    def deleteHost(self):
        listItems=self.ui.hostBrowser.selectedItems()
        if not listItems: return
        for item in listItems:
            with open(HOST, 'r') as f:
                hostLines = f.readlines()
            with open("src/writehost.txt", "r") as f:
                lines = f.readlines()
            with open("src/writehost.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != self.ui.hostBrowser.currentItem().text().strip("\n"):
                        f.write(line)
            with open("src/writehost.txt", "r") as f:
                linesAfterDelete = f.readlines()
            with open(HOST, 'w') as f:
                for hostLine in hostLines:
                    f.write(hostLine)
                    if hostLine.strip('\n') == "#DO NOT DELETE THIS LINE!!! IT'S USED BY HOST READER!":
                        f.write('\n'.join(linesAfterDelete))
                        break
            self.ui.hostBrowser.takeItem(self.ui.hostBrowser.row(item))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
