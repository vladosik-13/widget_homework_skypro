from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input: str) -> str:
    """Функция принимающая номер карты или счета и возвращающая замаскированную строку"""
    user_input_list = user_input.split()
    name_account_parts = []
    account_to_mask = ""
    for i in user_input_list:
        if i.isalpha():
            name_account_parts.append(i)
        elif i.isdigit and len(i) == 20:
            account_to_mask = get_mask_account(i)
        elif i.isdigit and len(i) == 16:
            account_to_mask = get_mask_account(i)
    name_account = ''.join(name_account_parts)
    return f"{name_account} {account_to_mask}"


num = input()
result = mask_account_card(num)
print(result)

from datetime import datetime


def get_date(date_str):
    """Функция принимающая дату в формате "2024-03-11T02:26:18.671407" и возвращающая дату в формате "11.03.2024" """
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


date_string = input()
formatted_date = get_date(date_string)
print(formatted_date)
