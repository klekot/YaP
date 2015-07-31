import sqlite3


def limit(count, db_path, req_date, day_limit, day_overdraft,
          limit_police, hour, search_work):
    day_limit_sum = 0
    conn = sqlite3.connect(db_path)
    db = conn.cursor()
    db.execute("select name from sqlite_master \
        where type='table' and name='limits'")
    if db.fetchone():
        db.execute(
            "select hour from limits where hour=? and date=?",
            (hour, req_date))
        if db.fetchone():
            db.execute("select counter from limits where hour=?", (hour,))
            counter = db.fetchone()[0]
            db.execute("select overdraft from limits where hour=?", (hour,))
            overdraft = db.fetchone()[0]
            db.execute("select overdraft from limits")
            for row in db.fetchall()[0]:
                day_overdraft += row
            db.execute("select counter from limits where date=?", (req_date,))
            for row in range(len(db.fetchall())):
                db.execute(
                    "select counter from limits where date=?", (req_date,))
                day_limit_sum += db.fetchall()[row][0]
        else:
            overdraft = 0
            counter = 0
            db.executemany(
                "insert into limits values (?, ?, ?, ?)",
                [(req_date, hour, counter, overdraft)])
            conn.commit()
            db.execute("select counter from limits where hour=?", (hour,))
            counter = db.fetchone()[0]
            db.execute("select overdraft from limits where hour=?", (hour,))
            overdraft = db.fetchone()[0]
            db.execute("select overdraft from limits")
            for row in db.fetchall()[0]:
                day_overdraft += row
            db.execute("select counter from limits where date=?", (req_date,))
            for row in range(len(db.fetchall())):
                db.execute(
                    "select counter from limits where date=?", (req_date,))
                day_limit_sum += db.fetchall()[row][0]
        db.close()
        conn.close()
    else:
        overdraft = 0
        counter = 0
        db.execute(
            "create table limits \
               (date data not null,\
                hour int not null, \
                counter int not null, \
                overdraft int not null)")
        db.executemany(
            "insert into limits values (?, ?, ?, ?)",
            [(req_date, hour, counter, overdraft)])
        conn.commit()
        db.close()
        conn.close()
    for i in range(len(limit_police)):
        if (hour in limit_police[i][1:]):
            tarif = i
    hour_limit = (limit_police[tarif][0] - (counter + 1) - overdraft)
    if search_work is True:
        if ((hour_limit > 0) and (counter < (day_limit - day_overdraft))):
            conn = sqlite3.connect(db_path)
            db = conn.cursor()
            counter += 1
            db.executemany(
                "update limits set counter=?, overdraft=? where hour=?",
                [(int(counter), 0, hour,)])
            conn.commit()
            db.close()
            conn.close()
            return True, hour_limit, day_limit_sum
        elif ((hour_limit <= 0) and (counter < (day_limit - day_overdraft))):
            conn = sqlite3.connect(db_path)
            db = conn.cursor()
            counter += 1
            db.executemany(
                "update limits set counter=?, overdraft=? where hour=?",
                [(int(counter), int((hour_limit) * (-1)), hour,)])
            conn.commit()
            db.close()
            conn.close()
            return False, hour_limit, day_limit_sum
        else:
            conn = sqlite3.connect(db_path)
            db = conn.cursor()
            counter += 1
            db.executemany(
                "update limits set counter=?, overdraft=? where hour=?",
                [(int(counter), int(hour_limit), hour,)])
            conn.commit()
            db.close()
            conn.close()
            return False, hour_limit, day_limit_sum
    else:
        return True, hour_limit + 1, day_limit_sum - 1
