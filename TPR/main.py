import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QFileDialog, QMainWindow)

from PandasModel import DataFrameModel
from Reduce import reduce
from Strategies import Strategies
from main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    matrix = pd

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.loadMenuItem.triggered.connect(self.loadFile)
        self.solveInStrategies.clicked.connect(self.solveInStrategies_)
        self.reduceBtn.clicked.connect(self.reduceMatrix)

    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')[0]
        self.matrix = pd.read_csv(fname, header=None)
        model = DataFrameModel(self.matrix)
        self.tableView.setModel(model)

    def solveInStrategies_(self):
        solving = Strategies.solveInClearStrategies(self.matrix)
        if solving is None:
            solving = Strategies.solveInMixedStrategies(self.matrix)
            print("Решено в смешанных стратегиях.")
        else:
            print("Решено в чистых стратегиях.")
            print(solving)

    def reduceMatrix(self):
        reduce(self.matrix)

        pass


app = QtWidgets.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec_())
