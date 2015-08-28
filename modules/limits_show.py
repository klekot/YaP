# -*- coding: utf-8 -*-


def limits_show(day_limit, limit_data,
                lcdNumber_hour_limit, lcdNumber_day_limit):
    lcdNumber_hour_limit.setProperty(
        "intValue", limit_data[1])
    lcdNumber_day_limit.setProperty(
        "intValue", (day_limit - limit_data[2]-1))
