import json


def get_transactions(file_path):
    """Функция принимает файл формата JSON, содержащий финанчовые транзакции и преобразует его в объект python,
      в данном случае в список словарей. если файл пустой, содержит не список или не найден,
      функция возвращает пустой список."""

    try:
         with open(file_path, encoding='utf-8') as f:
           data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    return data


# раскоментируй код ниже чтобы проверить функцию
# operation = get_transactions('C:/Users/user/PycharmProjects/home_work_widget/data/operations.json')
# print(operation)


if __name__ == '__utils__':
    utils()
