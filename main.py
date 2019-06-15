from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from main1 import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from excluded import Excluded


class MyApp(QtWidgets.QMainWindow):
    excludes = pyqtSignal(list)
    global HOST

    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        HOST = "/etc/hosts"
    else:
        HOST = "C:\\Windows\\System32\\drivers\\etc\\hosts"

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window = Excluded(self.excludes)
        self.init_ui()
        self.ui.addBtn.clicked.connect(self.add_host)
        self.ui.deleteBtn.clicked.connect(self.delete_host)
        self.ui.excludeBtn.clicked.connect(self.exclude_host)
        self.ui.removeFromExclude.clicked.connect(self.open_excludes)
        self.window.includes[list].connect(self.init_ui)

    def init_ui(self):
        self.setFixedSize(475, 372)
        self.setWindowTitle('Host Reader')
        lines = []
        exists = os.path.isfile('hosts.bak')
        if not exists:
            with open(HOST, 'r') as f:
                back_up = f.readlines()
            for backUpLine in back_up:
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

    def open_excludes(self):
        self.window.show()

    def add_host(self):
        text = self.ui.hostEditor.toPlainText()
        with open(HOST, 'a') as f:
            f.write(text + '\n')
        for line in text.split('\n'):
            self.ui.hostBrowser.addItem(line + '\n')
        self.ui.hostEditor.clear()
        self.ui.hostBrowser.scrollToBottom()
        self.ui.hostBrowser.show()

    def exclude_host(self):
        list_items = self.ui.hostBrowser.selectedItems()
        if not list_items: return
        exclude_list = []
        for item in list_items:
            with open(HOST, 'r') as f:
                host_lines = f.readlines()
            with open(HOST, 'w') as f:
                for hostLine in host_lines:
                    if hostLine.strip('\n') == item.text().strip('\n'):
                        f.write('#HE ' + hostLine)
                    else:
                        f.write(hostLine)
            exclude_list.append(item.text())
            self.ui.hostBrowser.takeItem(self.ui.hostBrowser.row(item))
        self.excludes.emit(exclude_list)

    def delete_host(self):
        list_items = self.ui.hostBrowser.selectedItems()
        if not list_items: return
        for item in list_items:
            print(item.text())
            with open(HOST, 'r') as f:
                host_lines = f.readlines()
            with open(HOST, 'w') as f:
                for line in host_lines:
                    if line.strip("\n") != item.text().strip("\n"):
                        f.write(line)
            self.ui.hostBrowser.takeItem(self.ui.hostBrowser.row(item))
        self.ui.hostBrowser.scrollToBottom()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
