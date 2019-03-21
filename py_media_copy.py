#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from pmc_ui import Ui_MainWindow
from pmc_ver import pmc_version
import sys

print(pmc_version)
testvar = "meine testvariable /home/bla"


class getvariable:
    def __init__(self):
        global testvar
        print("class getvariable:")
        print(testvar)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        global pmc_version
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textedit_outputconsole.append(pmc_version)
        # self.ui.lineEdit.setText("Template test")
        # self.ui.lineEdit.setMaxLength(25)
        self.ui.textedit_source.setText("Template test\nhallo")
        self.ui.pushbutton_start.clicked.connect(self.startBtnClicked)
        self.ui.pushbutton_exit.clicked.connect(self.close)

    def startBtnClicked(self):
        global testvar
        self.ui.textedit_outputconsole.append("button")
        testvar = self.ui.textedit_source.toPlainText()
        getvariable()


app = QtWidgets.QApplication([])
application = mywindow()

application.ui.textedit_target.setText(testvar)
application.show()

sys.exit(app.exec())
