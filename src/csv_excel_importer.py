import csv

import pandas as pd


def csv_import(path_file):
    """Функция принимает аргументом путь к файлу .csv и возвращает список словарей с транзакциями"""
    transactions = []
    try:
        with open(path_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)    # закоментируй строку чтобы выодилась первая строка тоже
            for row in reader:
                transactions.append(row)
    except Exception as e:
        print(f"Ошибка при считывании файла: {e}")
    return transactions


# раскоментируй код ниже чтобы проверить работу функции
'''test_func = csv_import('C:/Users/user/PycharmProjects/home_work_widget/data/transactions.csv')
print(test_func)'''


def excel_import(path_file):
    """Функция принимает аргументом путь к файлу Excel и возвращает список словарей с транзакциями, в котором ключами
     служат названия столбцов"""
    try:
        excel_data = pd.read_excel(path_file)
        # раскоментируй код нижк чтобы вывести данне о кол-ве строк и столбцов
        # print(excel_data.shape)

        # раскоментируй код нижк чтобы вывести пример данных таблицы
        # print(excel_data.head())

        # Преобразовывает каждую строку DataFrame в словарь, в котором ключами служат названия столбцов.
        transactions = excel_data.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при считывании файла: {e}")
        return []


# раскоментируй код ниже чтобы проверить работу функции
'''test_func = excel_import('C:/Users/user/PycharmProjects/home_work_widget/data/transactions_excel.xlsx')
print(test_func)'''
