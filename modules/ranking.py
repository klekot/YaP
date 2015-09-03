# -*- coding: utf-8 -*-

from modules.limits_show import limits_show


def ranking(r, rate_url, rank, res_list, query, req_date,
            day_limit, limit_data,
            lcdNumber_hour_limit, lcdNumber_day_limit):
    result = r.text
    result_list = result.split('<url>')
    for i, item in enumerate(result_list):
        if rate_url in item:
            rank += i
            break
    limits_show(day_limit, limit_data,
                lcdNumber_hour_limit, lcdNumber_day_limit)
    res_list.append((
        query.encode('utf-8').decode('cp1251', errors='replace'),
        rank,
        req_date,))
