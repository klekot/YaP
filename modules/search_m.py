# -*- coding: utf-8 -*-

from datetime import datetime
import time
from modules.sql_con import sql_con
from modules.remove_empty_rows import remove_empty_rows
from modules.limit import limit
from modules.coreFunction import coreFunction


def qCount(table_list):
    q_count = 0  # это кол-во запросов на обработку
    for i, item in enumerate(table_list):
        # смотрим, не был ли уже отработан текущий запрос
        if (table_list[i][1] != True):
            # итерируем кол-во запросов на обработку
            q_count += 1
    return q_count


def search(search_work, table_list, query, query_url,
           db_path, req_date, day_limit, day_overdraft, limit_police, hour,
           res_list, rank, label_info, table_results, rate_url,
           lcdNumber_hour_limit, lcdNumber_day_limit, progressBar,
           value, log, limit_data):
    # поднимаем флаг search_work для подсчёта лимитов
    search_work = True
    q_able = qCount(table_list) - limit_data[1]
    q_next = 0
    print(q_able)
    # ########################################################################
    # анализируем список запросов
    for i, item in enumerate(table_list):
        query = item[0]
        # если запрос не пустой начинаем его обработку
        if (len(query) != 0):
            # получаем данные по текущим лимитам на кол-во запросов
            limit_data = limit(db_path, req_date, day_limit,
                               day_overdraft, limit_police, hour,
                               search_work)
            if (q_able > 0):
                coreFunction(
                    query_url, query, progressBar, value, rate_url,
                    rank, res_list, req_date, day_limit, limit_data,
                    table_list, table_results, lcdNumber_hour_limit,
                    lcdNumber_day_limit, db_path, log, item,
                    label_info)
                q_able -= 1
                q_next += 1
                print(q_able)
            else:
                label_info.setText(
                    'Превышен лимит запросов!\nПродолжим через ' +
                    str(61 - int(datetime.now().strftime('%M'))) +
                    ' минут.')
                print("overload")
                # лимит в этом часу исчерпан,
                # но суточный еще доступен
                remove_empty_rows(1, table_results)
                print("sleep")
                # time.sleep(10.0)
                time.sleep((61 - int(
                    datetime.now().strftime('%M'))) * 60.0)
                q_able = q_next
                print(q_able)
                continue
            sql_con(db_path, res_list, query, req_date)
            res_list = []
            rank = 0
        else:
            # в случае пустого запроса
            label_info.setText(
                'Внимание!\nБыл выбран пустой запрос.')
            remove_empty_rows(1, table_results)
            continue
    search_work = False
