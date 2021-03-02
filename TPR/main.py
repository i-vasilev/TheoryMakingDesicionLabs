import os
import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QFileDialog, QMainWindow)

from PandasModel import DataFrameModel
from main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.loadMenuItem.triggered.connect(self.loadFile)

    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')[0]
        matrix = pd.read_csv(fname)
        model = DataFrameModel(matrix)
        self.tableView.setModel(model)


app = QtWidgets.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec_())
