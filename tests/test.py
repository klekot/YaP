from datetime import datetime
import sqlite3


hour = 12
db_path = 'keywords.db'
yandex_limits = [
    [0,  230, 0],  [1,  276, 0],  [2,  276, 0],
    [3,  276, 0],  [4,  276, 0],  [5,  230, 0],
    [6,  161, 0],  [7,  92,  0],  [8,  46,  0],
    [9,  46,  0],  [10, 46,  0],  [11, 46,  0],
    [12, 46,  0],  [13, 46,  0],  [14, 46,  0],
    [15, 46,  2],  [16, 46,  0],  [17, 46,  0],
    [18, 46,  0],  [19, 46,  0],  [20, 92,  0],
    [21, 161, 0],  [22, 230, 0],  [23, 240, 0]
]
summary_over = 0
for i in range(24):
    summary_over = summary_over + yandex_limits[i][2]


def limit(count):
    hour = datetime.now().strftime('%H')
    conn = sqlite3.connect(db_path)
    db = conn.cursor()
    db.execute("select name from sqlite_master \
        where type='table' and name='limits'")
    if db.fetchone():
        db.execute("select quantity from limits where hour=? and overdraft=0", hour)
        q_allowed = int(db.fetchone())
        hour_limit = (q_allowed - count)
        if ((hour_limit > 0) and (count < 460)):
            return True, hour_limit
        else:
            return False, hour_limit
    else:
        db.execute("create table limits (hour, quantity, overdraft)")
        db.executemany(
            "insert into limits values (?, ?, ?)",
            yandex_limits)
    db.close()
    conn.close()


if __name__ == '__main__':
    # hour = datetime.now().strftime('%H')
    hour = 12
    limit_police = [[230, 0, 5, 22, 23],
                    [276, 1, 2, 3, 4],
                    [161, 6, 21],
                    [92, 7, 20],
                    [46, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    print(hour)
    print(limit_police[0][1:])
    print(len(limit_police))
    print(limit(10))
