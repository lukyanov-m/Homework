import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected


def test_get_mask_card_number_with_invalid_number(invalid_values):
    for invalid_value in invalid_values:
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_value)


def test_get_mask_card_number_with_invalid_type(invalid_types):
    for invalid_type in invalid_types:
        with pytest.raises(TypeError):
            get_mask_card_number(invalid_type)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
        ("00000000000000000000", "**0000")
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_with_invalid_number(invalid_values):
    for invalid_value in invalid_values:
        with pytest.raises(ValueError):
            get_mask_account(invalid_value)


def test_get_mask_account_with_invalid_type(invalid_types):
    for invalid_type in invalid_types:
        with pytest.raises(TypeError):
            get_mask_account(invalid_types)
