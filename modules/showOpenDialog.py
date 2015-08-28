# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import xlrd
from modules.table_input import table_input


def showOpenDialog(YaP, fname, label_filepath, label_info,
                   btn_search, table_list, table_indexes,
                   table_add, table_row, table_results):
    # обнулили отображаемый путь к файлу xls
    label_filepath.setText('')
    # обнулили информацию в окне программы
    label_info.setText('')
    # вызываем диалог выбора файла
    fname, _ = QtWidgets.QFileDialog.getOpenFileName(
        YaP, 'Open file',
        'C:\\Users\\gnato\\Desktop\\Igor\\progs\\python_progs\\YaP\\')
    if len(fname) > 0:
        book = xlrd.open_workbook(fname, 'rt', formatting_info=True)
        sh = book.sheet_by_index(0)
        btn_search.setDisabled(False)
    else:
        # обработали вариант когда выбор файла отменён
        label_info.setText('Файл не выбран!')
        return
    # список уже ранее добавленных позиций
    table_list_items = []
    for item in table_list:
        table_list_items.append(item[0])
    # помещаем  ранее не внесённые запросы из файла в список
    for i in range(sh.nrows):
        if sh.cell_value(i, 0) not in table_list_items:
            table_list.append([sh.cell_value(i, 0), False])
    for i in range(len(table_list)):
        table_indexes.append(i)
    data_source = 'file'
    table_input(table_list, table_row, table_results, data_source)
    # формируем строку для отображения пути к оркрытому xls-файлу
    ################################################################
    fname_chars = []
    for char in fname:
        if (char == '/'):
            fname_chars.append('\\')
        else:
            fname_chars.append(char)
    win_path = ''.join(fname_chars)
    label_filepath.setText(win_path)
    #################################################################
