import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize("number_card, result", [("1596837868705199", "1596 83** **** 5199"),
                                                ("7158300734726758", "7158 30** **** 6758"),
                                                ("0000000000000000", "0000 00** **** 0000")])
def test_get_mask_card_number(number_card, result):
    assert get_mask_card_number(number_card) == result


def test_get_mask_card_number_with_invalid_number(invalid_values):
    for invalid_value in invalid_values:
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_value)


def test_get_mask_card_number_with_invalid_type(invalid_types):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_types)

