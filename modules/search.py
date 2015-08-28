# -*- coding: utf-8 -*-

from datetime import datetime
from modules.remove_empty_rows import remove_empty_rows
from modules.limit import limit
from modules.coreFunction import coreFunction


def search(search_work, table_list, query, query_url,
           db_path, req_date, day_limit, day_overdraft, limit_police, hour,
           res_list, rank, label_info, table_results, rate_url,
           lcdNumber_hour_limit, lcdNumber_day_limit, progressBar,
           value, log, btn_search, lineEdit_single_query, btn_input,
           circle, new_limit):
    # ########################################################################
    # query = table_list[len(table_list)-1][0]
    # если запрос не пустой начинаем его обработку
    if (len(query) != 0):
        # получаем данные по текущим лимитам на кол-во запросов
        limit_data = limit(db_path, req_date, day_limit,
                           day_overdraft, limit_police, hour,
                           search_work, 1, circle, new_limit)
        # print('search: limit_data[1] is ', end='')
        # print(limit_data[1])
        if (limit_data[1] > 1):
            # поднимаем флаг search_work для подсчёта лимитов
            search_work = True
            limit_data = limit(db_path, req_date, day_limit, day_overdraft,
                               limit_police, hour, search_work, 0,
                               circle, new_limit)
            coreFunction(
                query_url, query, progressBar, value, rate_url,
                rank, res_list, req_date, day_limit, limit_data,
                table_list, table_results, lcdNumber_hour_limit,
                lcdNumber_day_limit, db_path, log,
                label_info)
            search_work = False
            # print("search: if >1: limit_data[1] is :", end='')
            # print(limit_data[1])
        elif (limit_data[1] == 1):
            # поднимаем флаг search_work для подсчёта лимитов
            search_work = True
            limit_data = limit(db_path, req_date, day_limit, day_overdraft,
                               limit_police, hour, search_work, 0,
                               circle, new_limit)
            coreFunction(
                query_url, query, progressBar, value, rate_url,
                rank, res_list, req_date, day_limit, limit_data,
                table_list, table_results, lcdNumber_hour_limit,
                lcdNumber_day_limit, db_path, log,
                label_info)
            search_work = False
            label_info.setText(
                    'Достигнут лимит запросов!\nПродолжим через ' +
                    str(60 - int(datetime.now().strftime('%M'))))
            btn_search.setDisabled(True)
            lineEdit_single_query.setDisabled(True)
            btn_input.setDisabled(True)
            # print("search: if ==1: limit_data[1] is :", end='')
            # print(limit_data[1])
        else:
            search_work = True
            limit_data = limit(db_path, req_date, day_limit, day_overdraft,
                               limit_police, hour, search_work, 1,
                               circle, new_limit)
            coreFunction(
                query_url, query, progressBar, value, rate_url,
                rank, res_list, req_date, day_limit, limit_data,
                table_list, table_results, lcdNumber_hour_limit,
                lcdNumber_day_limit, db_path, log,
                label_info)
            search_work = False
            # print("self.table_list after search ", end='')
            # print(table_list)
    else:
        # в случае пустого запроса
        label_info.setText(
            'Внимание!\nБыл выбран пустой запрос.')
        remove_empty_rows(1, table_results)
    res_list = []
    rank = 0
    # print('search: go out')
    return limit_data[1]
