from src.widget import get_date, mask_account_card


def test_mask_account_card(card):
    assert mask_account_card("Visa Platinum 7000792289606361") == card


def test_2_mask_account_card(two_card):
    assert mask_account_card("Счет 73654108430135874305") == two_card


def test_get_date(date):
    assert get_date("2024-03-11T02:26:18.671407") == date
