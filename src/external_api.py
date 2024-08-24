import json
import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной APILAYER_API_KEY из .env-файла
API = os.getenv('APILAYER_API_KEY')


def get_transaction_amount(transaction):
    """принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float
    . Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
     конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь Exchange Rates Data API"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        pay = transaction["operationAmount"]["amount"]
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=rub&from=eur&amount={pay}'

        payload = {}
        headers = {
            "apikey": f"{API}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        pay = transaction["operationAmount"]["amount"]

        status_code = response.status_code
        result = response.text
        data_dict = json.loads(result)       # конвертируем полученный результат из стороннего сервиса конв. валют
        convert_pay = data_dict['result']    # выдераем из возврата стороннего конвертатора итоговое значение
        return convert_pay
    elif transaction["operationAmount"]["currency"]["code"] == "USD":
        pay = transaction["operationAmount"]["amount"]
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=rub&from=eur&amount={pay}'

        payload = {}
        headers = {
            "apikey": f"{API}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        pay = transaction["operationAmount"]["amount"]

        status_code = response.status_code
        result = response.text
        data_dict = json.loads(result)      # конвертируем полученный результат из стороннего сервиса конв. валют
        convert_pay = data_dict['result']   # выдераем из возврата стороннего конвертатора итоговое значение
        return convert_pay


test = get_transaction_amount({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
})
print(test)


if __name__ == '__external_api__':
    external_api()
