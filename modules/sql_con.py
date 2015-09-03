# -*- coding: utf-8 -*-

import sqlite3


def sql_con(db_path, res_list, query, req_date):
    conn = sqlite3.connect(db_path)
    # print('sql_con.py db connect')
    db = conn.cursor()
    db.execute("select name from sqlite_master \
        where type='table' and name='requests'")
    if db.fetchone():
        for res in res_list:
            k = (query.encode('utf-8').decode('cp1251', errors='replace'),
                 req_date,)
            db.execute("select * from requests \
                    where keyword=? and date=?", k)
            if db.fetchone():
                db.execute("delete from requests \
                    where keyword=? and date=?", k)
            else:
                continue
        db.executemany(
            "insert into requests values (?, ?, ?)",
            res_list)
    else:
        db.execute("create table requests (keyword, position, date)")
        db.executemany(
            "insert into requests values (?, ?, ?)",
            res_list)
    conn.commit()
    db.close()
    conn.close()
    # print('sql_con.py db close')
