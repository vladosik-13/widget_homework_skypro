import pytest


from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ('7000792289606361', '700079******6361'),
    ('0000000000000000', '000000******0000'),
    ('00000000000000000', 'номер карты должен состоять из 16 цифр'),
],)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('73654108430135874305', '**4305'),
    ('7365410843013587430509', 'номер счета должен состоять из 20ти цифр'),
],)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
