import re

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox

from mydesign import Ui_MainWindow
from math import sqrt
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.root.setText("")
        self.onlyInt = QIntValidator()
        self.ui.a.setValidator(self.onlyInt)
        self.ui.b.setValidator(self.onlyInt)
        self.ui.c.setValidator(self.onlyInt)
        self.ui.pushButton.clicked.connect(self.roots)

    def roots(self):
        a = self.ui.a.text()
        b = self.ui.b.text()
        c = self.ui.c.text()
        a = int(a)
        b = int(b)
        c = int(c)

        disk = b ** 2 - 4 * a * c
        if disk < 0:
            string = "Немає дійсних коренів."
        elif disk == 0:
            x = -b / 2 / a
            x = round(x, 2)
            string = "x=" + str(x)
        else:
            x1 = (-b - sqrt(disk)) / 2 / a
            x2 = (-b + sqrt(disk)) / 2 / a
            x1 = round(x1, 2)
            x2 = round(x2, 2)
            string = "x1=" + str(x1) + "\nx2=" + str(x2)
        self.ui.root.setText(string)


app = QtWidgets.QApplication([])
application = mywindow()
application.setWindowTitle("Квадратне рівняння")
application.show()

sys.exit(app.exec())
