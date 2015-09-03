# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sqlite3
from modules.remove_empty_rows import remove_empty_rows


def display_results(
        db_path, query, req_date, table_row, table_results, data_source, search_count):
    call_count = 1
    conn = sqlite3.connect(db_path)
    # print('display_results.py db connect')
    db = conn.cursor()
    k = (query.encode('utf-8', errors='replace').decode('cp1251', errors='replace'), req_date,)
    db.execute("select * from requests where keyword=? and date=?", k)
    arr = []
    for res in db.fetchone():
        if res != 0:
            arr.append(res)
        else:
            arr.append('> 100')
    for i in range(len(arr)):
        if (data_source == 'file'):
            table_results.setRowCount(table_row + 1)
            table_results.setItem(table_row, i, QtWidgets.QTableWidgetItem(str(arr[i]).encode('cp1251', errors='replace').decode('utf-8', errors='replace')))
        elif (data_source == 'line'):
            # print('display_results')
            # print(table_row)
            # print(call_count)
            # print(search_count)
            table_results.setRowCount(table_row + call_count + search_count)
            table_results.setItem(table_row + search_count, i, QtWidgets.QTableWidgetItem(str(arr[i]).encode('cp1251', errors='replace').decode('utf-8', errors='replace')))
    call_count += 1
    search_count += 1
    db.close()
    conn.close()
    # print('display_results.py db close')
    remove_empty_rows(1, table_results)
    return search_count
