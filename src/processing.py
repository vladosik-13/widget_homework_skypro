def filter_by_state(status_operation, state='EXECUTED'):
    """Функция фильтрвции по ключу state (по умолчанию ключ = 'EXECUTED')"""
    filtered_list = [operation for operation in status_operation if operation.get('state', 'EXECUTED') == state]
    return filtered_list

status_operation = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_list = filter_by_state(status_operation)
print(filtered_list)

