import sqlite3


def limit(db_path, req_date, day_limit, day_overdraft,
          limit_police, hour, search_work, compensation,
          new_limit, circle):
    day_counter_sum = 0
    conn = sqlite3.connect(db_path)
    # print('limit.py db connect')
    db = conn.cursor()
    db.execute("select name from sqlite_master \
        where type='table' and name='limits'")
    if db.fetchone():
        # print("limit: if db.fetchone()")
        db.execute(
            "select hour from limits where hour=? and date=?",
            (hour, req_date))
        if db.fetchone():
            db.execute(
                "select counter from limits where hour=? and date=?", (
                    hour, req_date))
            counter = db.fetchone()[0]
            db.execute(
                "select overdraft from limits where hour=? and date=?", (
                    hour, req_date))
            overdraft = db.fetchone()[0]
            db.execute("select overdraft from limits")
            for row in db.fetchall()[0]:
                day_overdraft += row
            db.execute("select counter from limits where date=?", (req_date,))
            for row in range(len(db.fetchall())):
                db.execute(
                    "select counter from limits where date=?", (req_date,))
                day_counter_sum += db.fetchall()[row][0]
                # print("limit: if: if: day_counter_sum is ", end="")
                # print(day_counter_sum)
        else:
            overdraft = 0
            counter = 0
            db.executemany(
                "insert into limits values (?, ?, ?, ?)",
                [(req_date, hour, counter, overdraft)])
            conn.commit()
            db.execute(
                "select counter from limits where hour=? and date=?", (
                    hour, req_date))
            counter = db.fetchone()[0]
            db.execute(
                "select overdraft from limits where hour=? and date=?", (
                    hour, req_date))
            overdraft = db.fetchone()[0]
            db.execute("select overdraft from limits")
            for row in db.fetchall()[0]:
                day_overdraft += row
            db.execute("select counter from limits where date=?", (req_date,))
            for row in range(len(db.fetchall())):
                db.execute(
                    "select counter from limits where date=?", (req_date,))
                day_counter_sum += db.fetchall()[row][0]
                # print("limit: if (else): day_counter_sum is ", end="")
                day_counter_sum
        db.close()
        conn.close()
        # print('limit.py db close')
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
        # print('limit.py db close')
    for i in range(len(limit_police)):
        if (hour in limit_police[i][1:]):
            tarif = i
    hour_limit = (limit_police[tarif][0] - (counter + 1) - overdraft)
    if search_work is True:
        if ((hour_limit > 0) and (counter < (day_limit - day_overdraft))):
            conn = sqlite3.connect(db_path)
            # print('limit.py db connect')
            db = conn.cursor()
            counter += 1
            db.executemany(
                "update limits set counter=?, \
                overdraft=? where hour=? and date=?",
                [(int(counter) + compensation, 0, hour, req_date)])
            conn.commit()
            db.close()
            conn.close()
            # print('limit.py db close')
            return [True, hour_limit, day_counter_sum]
        elif ((hour_limit <= 0) and (counter < (day_limit - day_overdraft))):
            conn = sqlite3.connect(db_path)
            # print('limit.py db connect')
            db = conn.cursor()
            counter += 1
            db.executemany(
                "update limits set counter=?, \
                overdraft=? where hour=? and date=?",
                [(int(counter) + compensation,
                    int((hour_limit) * (-1)), hour, req_date)])
            conn.commit()
            db.close()
            conn.close()
            # print('limit.py db close')
            return [False, hour_limit, day_counter_sum]
        else:
            conn = sqlite3.connect(db_path)
            # print('limit.py db connect')
            db = conn.cursor()
            counter += 1
            db.executemany(
                "update limits set counter=?, \
                overdraft=? where hour=? and date=?",
                [(int(counter) + compensation,
                    int(hour_limit), hour, req_date)])
            conn.commit()
            db.close()
            conn.close()
            # print('limit.py db close')
            return [False, hour_limit, day_counter_sum]
    else:
        return [True, hour_limit + 1, day_counter_sum - 1]
