# -*- coding: utf-8 -*-

import requests
from modules.ranking import ranking
from modules.sql_con import sql_con
from modules.display_results import display_results
from modules.pbarThread import pbarThread
import ssl
from functools import wraps


def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)


def coreFunction(query_url, query, progressBar, value, rate_url, rank,
                 res_list, req_date, day_limit, limit_data, table_list,
                 table_results, lcdNumber_hour_limit, lcdNumber_day_limit,
                 db_path, log, label_info):
    pBar = pbarThread(progressBar, value)
    pBar.start()
    r = requests.get(
        (query_url + query),
        verify="C:\\Python34\\Lib\\site-packages\\requests\\cacert.pem")
    ranking(r, rate_url, rank, res_list, query, req_date,
            day_limit, limit_data,
            lcdNumber_hour_limit, lcdNumber_day_limit)
    sql_con(db_path, res_list, query, req_date)
    display_results(db_path, query, req_date,
                    len(table_list), table_results)
    pBar.stop()
    log.write('Поиск из GUI по запросу "' + query + '";\n')
    table_list[len(table_list)-1][1] = True
    res_list = []
    rank = 0
    label_info.setText('Ваш запрос обработан.')
