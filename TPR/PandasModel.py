from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QModelIndex

Qt = QtCore.Qt


class DataFrameModel(QtCore.QAbstractTableModel):
    markY = -1
    markX = -1

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
            if role == Qt.BackgroundColorRole:
                if (index.row() == self.markY) & (index.column() == self.markX):
                    return QtGui.QColor("green")
        return QtCore.QVariant()

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.items = self.items[:position] + self.items[position + rows:]
        self.endRemoveRows()
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.items.insert()
            self.added += 1
        self.endInsertRows()
        return True
