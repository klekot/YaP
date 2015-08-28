# -*- coding: utf-8 -*-


def remove_empty_rows(col, table_results):
    for i in range(table_results.rowCount()):
        if (table_results.item(i, col) == None):
            table_results.removeRow(i)
