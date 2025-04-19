import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize("number_card, result", [("1596837868705199", "1596 83** **** 5199"),
                                                ("7158300734726758", "7158 30** **** 6758"),
                                                ("6831982476737658", "6831 98** **** 7658")])
def test_get_mask_card_number(number_card, result):
    assert get_mask_card_number(number_card) == result