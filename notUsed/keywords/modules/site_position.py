# -*- coding: utf-8 -*-


def site_position(result_html, rate_url):
    result_arr = []
    position = 0
    for text in result_html:
        result_arr.append(text)
    result_arr = result_arr[1:len(result_arr) - 1]
    result_string = "".join(result_arr)
    sep_string = result_string.split('><')
    rate_number = 0
    for i, item in enumerate(sep_string):
        if "b-link b-link_cropped_no serp-item__title-link" in item:
            rate_number += 1
            if rate_url in item:
                position = rate_number
    return position

if __name__ == '__main__':
    html = '< b-link b-link_cropped_no serp-item__title-link >< b-link b-link_cropped_no serp-item__title-link poligon.info>'
    url = 'poligon.info'
    print (site_position(html, url))
