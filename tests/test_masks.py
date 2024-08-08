from src.masks import get_mask_card_number



def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '700079******6361'


from src.masks import get_mask_account



def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'