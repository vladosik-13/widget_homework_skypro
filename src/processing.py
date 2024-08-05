def filter_by_state(status_operation, state="EXECUTED"):
    """Функция фильтрвции по ключу state (по умолчанию ключ = 'EXECUTED')"""
    filtered_list = [operation for operation in status_operation if operation.get("state", "EXECUTED") == state]
    return filtered_list


# раскомментируйте код ниже для проверки функции
# status_operation = [
#    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
#
# filtered_list = filter_by_state(status_operation)
# print(filtered_list)

from datetime import datetime


def sort_list_by_date(sorted_list, reverse=True):
    """Функция сортировки словаря по дате"""
    sorted_list.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
    return sorted_list


# Пример использования
# sorted_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# sorted_list_by_date_desc = sort_list_by_date(sorted_list)
# print(sorted_list_by_date_desc)
