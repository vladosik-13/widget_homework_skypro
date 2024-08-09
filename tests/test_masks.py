from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number) -> None:
    assert get_mask_card_number('7000792289606361') == card_number


def test_get_mask_account(mask_account) -> None:
    assert get_mask_account('73654108430135874305') == mask_account
