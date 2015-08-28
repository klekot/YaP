# -*- coding: utf-8 -*-

from yandex_parser import YandexParser
import requests
from codecs import *


# формируем запрос
file_name = 'result.html'
cookies_file = 'cookies.txt'
rate_url = 'poligon.info'
engine = 'yandex.ru'
query = 'реле интерфейсное'
res_per_page = 100
###############################################################
s_engine = 'http://' + engine + '/search/?text='
result_all = ''
page_iterator = 0
num_doc = '&numdoc=' + str(res_per_page)
next_page = ''
link_counter = 0
circle_count = 1  # задаём кол-во циклов прохода по результатам
request_address = s_engine + query + next_page + num_doc

r = requests.get('https://yandex.ru/search/xml?user=webmaster-poligon&key=03.279908682:25776a70171503eb70359c5bd5b820dc&l10n=ru&query=' + query)
result = r.text.encode('utf-8')
print result
#snippets = YandexParser(result, 'poligon.info').get_snippets()
#print snippets