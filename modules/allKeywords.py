# -*- coding: utf-8 -*-

import sqlite3


def allKeywords(db_path):
    allKeywords = []
    conn = sqlite3.connect(db_path)
    # print('allKeywords.py db connect')
    db = conn.cursor()
    db.execute("select name from sqlite_master \
        where type='table' and name='requests'")
    if db.fetchone():
        db.execute("select keyword from requests")
        for i in db.fetchall():
            if i[0].encode('cp1251', errors='replace').decode('utf-8', errors='replace') not in allKeywords:
                allKeywords.append(i[0].encode('cp1251', errors='replace').decode('utf-8', errors='replace'))
    else:
        allKeywords.append("")
    db.close()
    conn.close()
    # print('allKeywords.py db close')
    return allKeywords
