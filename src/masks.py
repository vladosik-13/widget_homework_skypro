import logging


logger = logging.getLogger('masks')    # создаем логер
logger.setLevel(logging.DEBUG)    # уровень вывода сообщения не меньше DEBUG
# создаем хендлер и указываем в какой папке будет лог и имя лога:
file_handler = logging.FileHandler('C:/Users/user/PycharmProjects/home_work_widget/logs/mask.log')
# создаем и настраиваем  форматтер логера:
file_formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)    # подключаем к логгеру форматтер
logger.addHandler(file_handler)    # подключаем к логгеру хендлер


def get_mask_card_number(x: str) -> str:
    logger.info(f'выполняем функцию маскировки номера банковской карты')
    """Функцию маскировки номера банковской карты"""
    hidden_number = x[:6] + "******" + x[12:]

    try:
        return hidden_number
    except:
        logger.error(f'номер карты должен состоять из 16 цифр')
        if len(x) != 16:
            return 'номер карты должен состоять из 16 цифр'


def get_mask_account(x: str) -> str:
    logger.info(f'выполняем функцию маскировки номера банковского счета')
    """Функцию маскировки номера банковского счета"""
    hidden_number = "**" + x[-4:]
    try:
        return hidden_number
    except:
        logger.error(f'произошла ошибка ввода')
        return []
