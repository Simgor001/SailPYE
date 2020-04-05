#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class core(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn = QtWidgets.QPushButton(self)
        self.btn.clicked.connect(self.close)
        self.btn.setText('Hello World!')
        self.btn.move(80, 80)
        self.resize(300, 200)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = core()
    sys.exit(app.exec_())
