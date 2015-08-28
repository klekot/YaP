from datetime import datetime
from modules.limit import limit
import sqlite3


conn = sqlite3.connect('keywords.db')
# print('initSettings.py db connect')
db = conn.cursor()
# сайт для которого рассситывается рейтинг
db.execute("select value from settings where variable='rate_url'")
rate_url = db.fetchone()[0]
# путь к файлу с базой данных sqlite3
db.execute("select value from settings where variable='db_path'")
db_path = db.fetchone()[0]
# путь к файлу с данными по рейтингам запросов
db.execute("select value from settings where variable='xls_path'")
xls_path = db.fetchone()[0]
# путь к файлу с логами запросов в программе
db.execute("select value from settings where variable='logs_path'")
logs_path = db.fetchone()[0]
# URL запроса к Яндексу
db.execute("select value from settings where variable='query_url'")
query_url = db.fetchone()[0]
# дневной лимит запросов, предоставленный Яндексом
db.execute("select `limit` from time_limits where times='all_day'")
day_limit = db.fetchone()[0]
# политика Яндекса по распределению лимитов по времени суток
# первая позиция - лимит запросов, следующие - это часы от 0 до 23,
# в течение которых действуют указанные лимиты
limit_police = []
arr = []
db.execute("select * from time_limits")
fetchall = db.fetchall()
for i in range(1, len(fetchall)):
    arr.append(int(fetchall[i][1]))
    arr.append(int(fetchall[i][0]))
    limit_police.append(arr)
    arr = []
limit_police = sorted(limit_police, key=lambda times: times[1])
db.close()
conn.close()
# ключевое слово, для которого вычисляется позиция в выдаче Яндекса
query = ''
# список результатов рейтинга
res_list = []
# позиция в выдаче Яндекса
rank = 0
# имя xls-файла для списка запросов и вывода по ним статистики рейтингов
fname = ''
# кол-во столбцов в таблице представления данных
# table_row = 0
# превышение лимита запросов за предыдущий день
day_overdraft = 0
# список запросов, отображаемых в таблице
table_list = []
# список номеров строк в таблице с текущими запросами
table_indexes = []
# сюда поступают одиночные запросы перед добавлением в таблицу
table_add = []
# переключатель для функции подсчёта лимитов(чтобы не считал вхолостую)
search_work = False

ref_path = "file:///C:/Users/gnato/Desktop/Igor/progs/python_progs/YaP/reference.html"
# текущий час суток
# формат: strftime('%Y-%m-%d %H:%M:%S')
hour = int(datetime.now().strftime('%H'))
req_date = str(datetime.now().strftime('%Y-%m-%d'))
# данные по текущим лимитам, заполняются возвратом от функции limit()
limit_data = limit(db_path, req_date, day_limit, day_overdraft,
                   limit_police, hour, search_work, 1, 0, 0)
