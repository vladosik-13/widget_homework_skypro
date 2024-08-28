import json
import logging

logger = logging.getLogger('utils')    # создаем логер
logger.setLevel(logging.DEBUG)    # уровень вывода сообщения не меньше DEBUG
# создаем хендлер и указываем в какой папке будет лог и имя лога:
file_handler = logging.FileHandler('C:/Users/user/PycharmProjects/home_work_widget/logs/utils.log')
# создаем и настраиваем  форматтер логера:
file_formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)    # подключаем к логгеру форматтер
logger.addHandler(file_handler)    # подключаем к логгеру хендлер


def get_transactions(file_path):
    """Функция принимает файл формата JSON, содержащий финанчовые транзакции и преобразует его в объект python,
      в данном случае в список словарей. если файл пустой, содержит не список или не найден,
      функция возвращает пустой список."""

    try:
        logger.info('выполняем функцию преобразования файла из json в python объект')
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        logger.error('произошла ошибка')
        return []

    if not isinstance(data, list):
        return []

    return data


# раскоментируй код ниже чтобы проверить функцию
# operation = get_transactions('C:/Users/user/PycharmProjects/home_work_widget/data/operations.json')
# print(operation)
# if __name__ == '__utils__':
#    utils()
