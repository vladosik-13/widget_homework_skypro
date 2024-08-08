from src.widget import mask_account_card


def test_mask_account_card():
    assert mask_account_card('Visa Platinum 7000792289606361') == 'VisaPlatinum **6361'


def test_2_mask_account_card():
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'

from src.widget import get_date


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
