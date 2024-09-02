import re


def search_transactions(transactions, search_string):
    """Функция принимает список словарей с данными о банковских операциях
    и строку поиска, а возвращает список словарей с соответствующими записями."""
    search_pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    result = [
        transaction for transaction in transactions
        if search_pattern.search(transaction.get('description', ''))
    ]
    return result


# раскоментируйте код ниже чтобы проверить ф-ю
'''transactions = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                 'to': 'Счет 64686473678894779589'},
                {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
                 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},
                {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542','to':
                 'Счет 75651667383060284188'}
]

search_string = 'Перевод со счета на счет'
filtered_transactions = search_transactions(transactions, search_string)
print(filtered_transactions)'''
