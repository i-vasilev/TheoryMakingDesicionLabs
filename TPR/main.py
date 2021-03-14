import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QFileDialog, QMainWindow)

import Strategies
from PandasModel import DataFrameModel
from Reduce import reduce
from main_window import Ui_MainWindow
from saddlePointsDialog import SaddlePointsDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    matrix = pd

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.loadMenuItem.triggered.connect(self.loadFile)
        self.solveInStrategies.clicked.connect(self.solveInStrategies_)
        self.reduceBtn.clicked.connect(self.reduce_matrix)
        self.makeMatrixBtn.clicked.connect(self.make_matrix)

    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')[0]
        if fname != "":
            self.matrix = pd.read_csv(fname, header=None)
            model = DataFrameModel(self.matrix)
            self.tableView.setModel(model)

    def set_cell_color(self, row, column):
        self.matrix.change_color(row, column, QColor(0, 127, 0))

    def solveInStrategies_(self):
        vec = Strategies.minimax(self.matrix)
        if vec is None:
            self.log.setText("Решения в чистых стратегиях не найдено. Введите седловые точки в смешанных стратегиях.")
            dialog = SaddlePointsDialog(parent=self)
            if dialog.show():
                p = int(dialog.pEdit.text())
                q = int(dialog.qEdit.text())

                self.log.setText("Решено в смешанных стратегиях")
        else:
            v1 = Strategies.maximin_strategies(self.matrix, vec)
            v2 = Strategies.minimax_strategies(self.matrix, vec)
            s = pd.DataFrame([[int(v1["i"]), int(v2["i"])],
                              [int(v1["i"]), int(v2["j"])],
                              [int(v1["j"]), int(v2["i"])],
                              [int(v1["j"]), int(v2["j"])]],
                             columns=["i", "j"])
            s = s + 1
            self.log.setText(str(s) + "\nЗначение игры в чистых стратегиях: V = " + str(self.matrix[vec[0]][vec[1]]))
            model = DataFrameModel(self.matrix)
            model.markX = vec[0]
            model.markY = vec[1]
            self.tableView.clearSpans()
            self.tableView.setModel(model)

    def make_matrix(self):
        dfm = DataFrameModel(pd.DataFrame.empty)
        dfm.insertRows(int(self.rowsBox.value()))
        # dfm.insertColumns(count=self.columnBox.value())

    def reduce_matrix(self):
        model = DataFrameModel(reduce(self.matrix))
        self.tableView.clearSpans()
        self.tableView.setModel(model)


app = QtWidgets.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec_())
