# -*- coding: utf-8 -*-

# выводим в таблицу список уникальных запросов из файла

from PyQt5 import QtWidgets
from modules.remove_empty_rows import remove_empty_rows

call_count = 1


def table_input(add_list, table_row, table_results, data_source, search_count, file_search_count):
    global call_count
    # список уже ранее добавленных позиций
    add_list_items = []
    for item in add_list:
        add_list_items.append(item[0])
    for i, item in enumerate(add_list):
        # print(call_count)
        # ################# working ####################
        if (data_source == 'file'):
            file_search_count = True
            # print("file")
            if (call_count == 1):
                if item[0] in add_list_items:
                    table_row += 1
                    table_results.setRowCount(table_row + 1)
                    table_results.setItem(table_row - 1, 0,
                                          QtWidgets.QTableWidgetItem(item[0]))
            else:
                if item[0] in add_list_items:
                    table_row += 1
                    table_results.setRowCount(table_row + 1)
                    table_results.setItem(table_row - 1, 0,
                                          QtWidgets.QTableWidgetItem(item[0]))
        elif (data_source == 'line'):
            # print("line")
            if (call_count == 1):
                if item[0] in add_list_items:
                    # print(table_row)
                    # print(call_count)
                    table_row += 1
                    table_results.setRowCount(table_row)
                    table_results.setItem(table_row - 1, 0,
                                          QtWidgets.QTableWidgetItem(item[0]))
            else:
                if item[0] in add_list_items:
                    # print(table_row)
                    # print(call_count)
                    # print(file_search_count)
                    if file_search_count:
                        table_row += 1
                        table_row += search_count - call_count + 1
                        table_results.setRowCount(table_row + 1)
                        table_results.setItem(table_row, 0,
                                              QtWidgets.QTableWidgetItem(item[0]))
                    else:
                        table_row += search_count - call_count + 1
                        table_results.setRowCount(table_row + 1)
                        table_results.setItem(table_row, 0,
                                              QtWidgets.QTableWidgetItem(item[0]))
                        # table_row += 1

        remove_empty_rows(0, table_results)
    call_count += 1
    return file_search_count
