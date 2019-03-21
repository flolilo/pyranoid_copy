#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from guitest import Ui_MainWindow
import versioning
import sys

print(versioning.py_media_copy_version)
testvar = "meine testvariable /home/bla"


class getvariable:
    def __init__(self):
        global testvar
        print("class getvariable:")
        print(testvar)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        global versioning
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.lineEdit.setText("Template test")
        # self.ui.lineEdit.setMaxLength(25)
        self.ui.textEdit.setText("Template test\nhallo")
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        global testvar
        self.ui.textEdit.append("button")
        testvar = self.ui.lineEdit.text()
        getvariable()


app = QtWidgets.QApplication([])
application = mywindow()

application.ui.lineEdit.setText(testvar)
application.show()

sys.exit(app.exec())
