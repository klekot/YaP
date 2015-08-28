import requests
import sys

rate_url = 'poligon.info'
query = 'таймер задержки включения'
rank = 0

r = requests.get('https://yandex.ru/search/xml?user=webmaster-poligon\
                  &key=03.279908682:25776a70171503eb70359c5bd5b820dc&l10n=ru\
                  &groupby=groups-on-page%3D100&query=' + query)
result = r.text
res_join = ''.join(result)
res_list = res_join.split('<url>')
for i, item in enumerate(res_list):
    if rate_url in item:
        rank += i
        break
with open('xml_file.txt', 'w', encoding='utf-8') as f:
    f.write(result)

if rank != 0:
    sys.stdout.buffer.write(('По запросу \"' + query + '\" сайт poligon.info\
                              \nнаходится на ' + str(rank) + '-й позиции.\
                              \n').encode('utf8'))
else:
    sys.stdout.buffer.write(('По запросу \"' + query + '\" сайт poligon.info\
                              \nнаходится ниже 100-й позиции.\
                              \n').encode('utf8'))
