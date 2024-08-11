import pytest


from src.masks import get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    ('7000792289606361', '700079******6361'),
    ('0000000000000000', '000000******0000'),],)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected
