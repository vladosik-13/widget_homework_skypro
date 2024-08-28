import csv
import pandas


def csv_import(path_file):
    """Функция принимает аргументом путь к файлу .csv и возвращает список словарей с транзакциями"""
    with open(path_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)    # закоментируй строку чтобы выодилась первая строка тоже
        for row in reader:
            print(row)


# раскоментируй код ниже чтобы проверить работу функции
"""test_func = csv_import('C:/Users/user/PycharmProjects/home_work_widget/data/transactions.csv')
print(test_func)"""


