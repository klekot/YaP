import sys
import requests
from codecs import *
from modules.site_position import *
import pickle


def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# формируем запрос
file_name = 'result.html'
cookies_file = 'cookies.txt'
rate_url = 'poligon.info'
engine = 'yandex.ru'
query = 'relequick'
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
# отправляем запрос
while (page_iterator < circle_count):
        # если это не первый запрос в цикле добавляем в него куки
    if page_iterator == 0:
        r = requests.get(request_address)
    else:
        r = requests.get(request_address, cookies=load_cookies(cookies_file))
    # сохраняем куки в файл для последующей отправки в запросе
    save_cookies(r.cookies, cookies_file)
    # получаем код страницы выдачи
    result = r.text
    link_counter += result.count('serp-item__wrap clearfix')
    page_iterator += 1
    # проверяем наличие пагинации
    if (result.find("<span class=\"pager__group\">") != -1):
        # пагинация найдена
        result_all += ' ' + result
        next_page = '&p=' + str(page_iterator)
    else:
        # пагинации нет
        # проверим причины отсутствия пагинации
        if (result.find("captcha") != -1):
            # словили капчу
            sys.stdout.buffer.write(("CAPTCHA!!!\n").encode('utf-8'))
            with open(file_name, "w", encoding='utf-8') as f:
                f.write(result)
            break
        elif (result.find("<title>404</title>") != -1):
            # пагинация закончилась
            # выходим из цикла
            sys.stdout.buffer.write(("пагинация закончилась\
                                     \n").encode('utf-8'))
        elif (result.find("query") != -1):
            # выдача поместилась на одной странице
            sys.stdout.buffer.write("одна страница").encode('utf-8')
with open('result_all.txt', 'w', encoding='utf-8') as ra:
    ra.write(result_all)
sys.stdout.buffer.write(("Страниц с результатами поиска: "
                         + str(page_iterator) + "\n").encode('utf-8'))
sys.stdout.buffer.write(("Общее количество сылок по запросу " +
                         '"' + query + '"' ": "
                         + str(link_counter) + "\n").encode('utf-8'))
if (site_position(result, rate_url) != 0):
    sys.stdout.buffer.write(("По запросу \"" + query + "\""
                             + " к поисковой системе \"" + engine.capitalize()
                             [0:6] + "\" сайт " + rate_url + " занимает " +
                             str(site_position(result, rate_url)) +
                             "-е место.\n").encode('utf-8'))
else:
    sys.stdout.buffer.write(("По запросу \"" + query + "\""
                             + " к поисковой системе \"" + engine.capitalize()
                             [0:6] + "\" сайт " + rate_url + "\nне попал в \
диапазон полученных результатов.\n").encode('utf-8'))
