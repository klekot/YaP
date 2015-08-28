# -*- coding: utf-8 -*-

import requests
from datetime import datetime
import time
from modules.ranking import ranking
from modules.sql_con import sql_con
from modules.display_results import display_results
from modules.remove_empty_rows import remove_empty_rows
from modules.pbarThread import pbarThread
from modules.limit import limit

import ssl
from functools import wraps


def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)


def search(search_work, table_list, query, query_url,
           db_path, req_date, day_limit, day_overdraft, limit_police, hour,
           res_list, rank, label_info, table_results, rate_url,
           lcdNumber_hour_limit, lcdNumber_day_limit, progressBar,
           value, log):
    pBar = pbarThread(progressBar, value)
    pBar.start()
    # поднимаем флаг search_work для подсчёта лимитов
    search_work = True
    q_count = 0
    # #####################################################################
    # анализируем список запросов
    for i, item in enumerate(table_list):
        query = item[0]
        worked = item[1]
        if ((query != '') or (worked is not True)):
            q_count += 1
            limit_data = limit(db_path, req_date, day_limit,
                               day_overdraft, limit_police, hour,
                               search_work)
            if q_count > limit_data[1]:
                label_info.setText('Превышен лимит запросов!\n\
                                    Продолжим через')  # timer
                label_info.setText(' минут.')
                remove_empty_rows(1, table_results)
                time.sleep((60 - int(
                    datetime.now().strftime('%M'))) * 60.0)
                continue
            else:
                # Проверяем не исчерпан ли суточный лимит на запросы.
                if (limit_data[2] >= 0):
                    # если не был - отправляем запрос в Яндекс
                    r = requests.get((query_url + query),
                       verify="C:\\Python34\\Lib\\site-packages\\requests\\cacert.pem")
                    pBar.stop()
                    # и помечаем запрос как отработанный
                    table_list[i][1] = True
                    # ранжируем запрос, записываем результат в БД
                    ranking(r, rate_url, rank, res_list, query, req_date,
                            day_limit, limit_data,
                            lcdNumber_hour_limit, lcdNumber_day_limit)
                    sql_con(db_path, res_list, query, req_date)
                    # обновляем табло лимитов
                    display_results(db_path, query, req_date,
                                    len(table_list), table_results)
                    log.write(
                        'Поиск по запросу "' + item[0] +
                        '";        \n')
                    res_list = []
                    rank = 0
                    label_info.setText('Ваш запрос обработан.')
                else:
                    # суточный лимит не доступен
                    label_info.setText(
                        'Превышен суточный \nлимит запросов!\nЗаходите завтра:)')
                    return
            sql_con(db_path, res_list, query, req_date)
            res_list = []
            rank = 0
        else:
            continue
    search_work = False
