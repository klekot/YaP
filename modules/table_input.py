# -*- coding: utf-8 -*-

# выводим в таблицу список уникальных запросов из файла

from PyQt5 import QtWidgets
from modules.remove_empty_rows import remove_empty_rows

call_count = 1


def table_input(add_list, table_row, table_results, data_source):
    clean_flag = False
    global call_count
    # список уже ранее добавленных позиций
    add_list_items = []
    for item in add_list:
        add_list_items.append(item[0])
    for i, item in enumerate(add_list):
        # ################# working ####################
        if (call_count == 1):
            if clean_flag:
                if data_source == 'file':
                    if item[0] in add_list_items:
                        table_results.setRowCount(table_row + 1)
                        table_results.setItem(
                            table_row, 0,
                            QtWidgets.QTableWidgetItem(item[0]))
                    table_row += 1
                else:
                    if item[0] in add_list_items:
                        table_row += 1
                        table_results.setRowCount(table_row + 1)
                        table_results.setItem(
                            table_row - 1, 0,
                            QtWidgets.QTableWidgetItem(item[0]))
            else:
                if item[0] in add_list_items:
                    table_row += 1
                    table_results.setRowCount(table_row + 1)
                    table_results.setItem(table_row, 0,
                                          QtWidgets.QTableWidgetItem(item[0]))
        else:
            if clean_flag:
                if item[0] in add_list_items:
                    table_results.setRowCount(table_row + 1)
                    table_results.setItem(table_row, 0,
                                          QtWidgets.QTableWidgetItem(item[0]))
                    table_row += 1
            else:
                if item[0] in add_list_items:
                    table_row += 1
                    table_results.setRowCount(table_row + 1)
                    table_results.setItem(table_row - 1, 0,
                                          QtWidgets.QTableWidgetItem(item[0]))

        remove_empty_rows(0, table_results)
    call_count += 1
