def get_mask_card_number(x: str) -> str:
    """Функцию маскировки номера банковской карты"""
    x = input()
    hidden_number = x[:6] + "******" + x[12:]
    return hidden_number


def get_mask_account(x: str) -> str:
    """Функцию маскировки номера банковского счета"""
    x = input()
    hidden_number = "****" + x[-4:]
    return hidden_number
