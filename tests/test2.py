            r = requests.get(self.query_url + self.query)
            self.r_count += 1
            self.limit_data = limit(
                                self.r_count, self.db_path, self.req_date,
                                self.day_limit, self.day_overdraft,
                                self.limit_police, self.hour, self.search_work)
            result = r.text
            result_list = result.split('<url>')
            for i, item in enumerate(result_list):
                if self.rate_url in item:
                    self.rank += i
                    break
            if self.rank != 0:
                self.cell_rank = str(self.rank)
            else:
                self.cell_rank = "< 100"
            self.cell_date = self.req_date
            # print(len(self.recent_requests))
            if (self.query not in self.recent_requests):
                self.cell_word = self.query
                self.recent_requests.append(self.query)
                self.table_results.setRowCount(self.table_row + 1)
                self.table_results.setItem(
                        self.table_row, 0,
                        QtWidgets.QTableWidgetItem(self.cell_word))
                self.table_results.setItem(
                        self.table_row, 1,
                        QtWidgets.QTableWidgetItem(self.cell_rank))
                self.table_results.setItem(
                        self.table_row, 2,
                        QtWidgets.QTableWidgetItem(self.cell_date))
                self.table_row += 1
                self.label_info.setText(
                        'Запрос обработан.\nДля сохранения статистики\nнажмите кнопку \"Сохранить\".')
            else:
                self.label_info.setText('Этот запрос уже обработан.\n\
                                        Введите другой запрос.')
            self.recent_limit = self.limit_data[1]
            self.lcdNumber_hour_limit.setProperty(
                "intValue", self.recent_limit)
            self.lcdNumber_day_limit.setProperty(
                "intValue", (self.day_limit - self.limit_data[2]-1))
            self.res_list.append((
                self.query.encode('utf-8').decode('cp1251'),
                self.rank,
                self.req_date,))
            self.sql_con(self.res_list)
            self.res_list = [] ######