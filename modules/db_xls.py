# -*- coding: utf-8 -*-

# все записи БД из таблицы request переносит в xls-файл

from xlwt import Workbook
from xlwt import easyxf
import sqlite3


def db_xls(db_path, xls_path, req_date):
    conn = sqlite3.connect(db_path)
    db = conn.cursor()
    wb = Workbook()
    ws = wb.add_sheet('keywords')
    plain = easyxf('')
    temp_arr = []
    temp_cols = []
    db.execute("select * from requests where date=?", (req_date,))
    for r, row in enumerate(db.fetchall()):
        if (row[0] not in temp_cols) and (row[0] != ''):
            temp_cols.append(row[0])
            temp_arr.append(row)
    for r, row in enumerate(temp_arr):
        for c, col in enumerate(row):
            if (type(col) is int) != True:
                ws.write(r, c, col.encode('cp1251')
                         .decode('utf-8'), plain)
            else:
                ws.write(r, c, col, plain)
        wb.save(xls_path)
    db.close()
    conn.close()
