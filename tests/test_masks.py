from src.masks import get_mask_card_number



def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '700079******6361'