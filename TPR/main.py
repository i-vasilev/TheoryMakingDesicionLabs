import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QFileDialog)

from IO.excelInput import get_matrix

matrix = 0
matrixGame = 0


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("res/main_window.ui", self)
        self.loadMenuItem.clicked.connect(self.loadFileBtnClicked)

    def loadFileBtnClicked(self):
        fname = QFileDialog.getOpenFileName(None, "Open file", os.getenv('HOME'))
        matrix = get_matrix(fname[0])
        self.matrixGame.data = matrix


app = QtWidgets.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec_())
