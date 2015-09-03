# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets


class TableWidget(QtWidgets.QTableWidget):

    def __init__(self, table_list, table_indexes, parent=None):
        self.table_list = table_list
        self.table_indexes = table_indexes

        QtWidgets.QTableWidget.__init__(self, parent)

    def contextMenuEvent(self, event):
        self.menu = QtWidgets.QMenu(self)
        renameAction = QtWidgets.QAction('Удалить из списка', self)
        renameAction.triggered.connect(self.del_row)
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QtGui.QCursor.pos())

    def del_row(self):
        rows = sorted(
            set(index.row() for index in self.selectedIndexes()))
        i = 0
        for row in rows:
            try:
                self.removeRow(row)
                self.table_list.pop(self.table_indexes[row] - i)
                i += 1
            except IndexError:
                pass
