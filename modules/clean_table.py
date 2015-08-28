# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from modules.Ui_YaP import Ui_YaP


def clean_table(checkBox, table_results, table_row, table_list):
    if checkBox.isChecked():
        table_results.setRowCount(0)
        table_results.setItem(0, 0, QtWidgets.QTableWidgetItem(''))
        table_results.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
        table_results.setItem(0, 2, QtWidgets.QTableWidgetItem(''))
        Ui_YaP.table_row = 0
        Ui_YaP.table_list = []
