# --*-- coding: utf-8 --*--

import time
from datetime import datetime
from modules.search import search


def searchDelay(search_work, table_list, item, query_url,
                db_path, req_date, day_limit, day_overdraft,
                limit_police, hour, res_list, rank, label_info,
                table_results, rate_url, lcdNumber_hour_limit,
                lcdNumber_day_limit, progressBar, value, log,
                btn_search, lineEdit_single_query, btn_input,
                waiting_queries):
    print("searchDelay: ", end='')
    if (len(waiting_queries) > 0):
        label_info.setText(
            'Запросы отложены!\nПродолжим через ' +
            str(60 - int(datetime.now().strftime('%M'))))
        btn_search.setDisabled(True)
        lineEdit_single_query.setDisabled(True)
        btn_input.setDisabled(True)
        print("sleep 10 sec.")
        # time.sleep(10)
        time.sleep((60 - int(datetime.now().strftime('%M'))) * 60.0)
        for item in waiting_queries:
            print("searchDelay: for: item is ", end='')
            print(item)
            search(search_work, table_list, item, query_url,
                   db_path, req_date, day_limit, day_overdraft, limit_police,
                   hour, res_list, rank, label_info, table_results, rate_url,
                   lcdNumber_hour_limit, lcdNumber_day_limit, progressBar,
                   value, log, btn_search, lineEdit_single_query, btn_input,
                   waiting_queries)
        waiting_queries = []
        return waiting_queries
        ''''
        searchDelay(search_work, table_list, item, query_url,
                    db_path, req_date, day_limit, day_overdraft,
                    limit_police, hour, res_list, rank, label_info,
                    table_results, rate_url, lcdNumber_hour_limit,
                    lcdNumber_day_limit, progressBar, value, log,
                    btn_search, lineEdit_single_query, btn_input,
                    waiting_queries)
		'''
