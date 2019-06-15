from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from exclude import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal


class Excluded(QtWidgets.QMainWindow):
    includes = pyqtSignal(list)
    global HOST

    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        HOST = "/etc/hosts"
    else:
        HOST = "C:\\Windows\\System32\\drivers\\etc\\hosts"

    def __init__(self, excludes):
        super(Excluded, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui1()

        self.ui.includeBtn.accepted.connect(self.remove)
        self.ui.includeBtn.rejected.connect(self.hide)
        excludes[list].connect(self.init_ui1)

    def init_ui1(self):
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
        list_items = self.ui.excludeBrowse.selectedItems()
        sending_value = []
        for item in list_items:
            with open(HOST, 'r') as f:
                excludes = f.readlines()
            with open(HOST, 'w') as f:
                for line in excludes:
                    if line.strip('\n').strip('#HE ') == item.text().strip('\n').strip('#HE '):
                        f.write(line.strip('#HE '))
                    else:
                        f.write(line)
            sending_value.append(item.text())
            self.ui.excludeBrowse.takeItem(self.ui.excludeBrowse.row(item))
        self.includes.emit(sending_value)
        self.hide()
