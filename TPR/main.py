import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
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

    def set_cell_color(self, row, column):
        self.matrix.change_color(row, column, QColor(0, 127, 0))

    def solveInStrategies_(self):
        solving = Strategies.solveInClearStrategies(self.matrix)
        if solving is None:
            solving = Strategies.solveInMixedStrategies(self.matrix)
            print("Решено в смешанных стратегиях.")
        else:
            self.log.setText("Решено в чистых стратегиях. Первому игроку следует играть стратегией "
                             + str(solving[0]) + ". Второму - стратегией " + str(solving[1]))

    def reduceMatrix(self):
        model = DataFrameModel(reduce(self.matrix))
        self.tableView.clearSpans()
        self.tableView.setModel(model)


app = QtWidgets.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec_())
