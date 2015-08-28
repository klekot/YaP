# -*- coding: utf-8 -*-

import requests
from codecs import *
import webbrowser
from modules.site_position import *

# формируем запрос
rate_url = 'poligon.info'
s_engine = 'https://www.google.ru/search?&q=' # Google
query = 'poligon' # Google
page_iterator = 0
res_per_page = 100 # max 100
next_page = '&num=' + str(res_per_page) + '&start=' + str(page_iterator)
link_counter = 0
# по умолчанию считаем, что пагинация есть,
# это нужно для запуска цикла
# pagination = True
circle_count = 1 # задаём кол-во циклов прохода по результатам

# отправляем запрос
# while (pagination): # вариант полного прохода по результатам - обычно не доходит до конца, ловит капчу
while (page_iterator < circle_count):
	r = requests.get(s_engine + query + next_page)
	# print str(r.headers)
	# получаем код страницы выдачи
	result = r.text.encode('utf-8', errors='replace')

	# проверяем наличие пагинации
	if (result.find("nav_logo225.png") != -1):
		# пагинация найдена
		print "пагинация найдена"
		page_iterator += 1
		next_page = '&num=' + str(res_per_page) + '&start=' + str(page_iterator * res_per_page)
		link_counter += result.count("<!--m-->")
		webbrowser.open_new_tab(s_engine + query + next_page)
	else:
		# пагинации нет
		# pagination = False
		page_iterator += 1
		# проверим причины отсутствия пагинации
		if (result.find("captcha") != -1):
			# словили капчу
			print "словили капчу"
			# webbrowser.open_new(result)
		elif (result.find("<div class=\"mnr-c\">") != -1):
			# пагинация закончилась
			# выходим из цикла
			print "пагинация закончилась"
		elif (result.find("<li class=\"g\">") != -1):
			# выдача поместилась на одной странице
			print "одна страница"
			link_counter += result.count("<!--m-->")

#with open("result.txt", "w") as f:
#	f.write(result)

print "Страниц с результатами поиска: " + str(circle_count)
print "Ссылок на странице: " + str(link_counter)
print str(site_position(result, rate_url)) + "-е место"