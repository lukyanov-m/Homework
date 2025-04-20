import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


def test_mask_account_card_with_invalid_data(invalid_values):
    for value in invalid_values:
        with pytest.raises(ValueError):
            mask_account_card(value)


def test_mask_account_card_with_invalid_type(invalid_types):
    for invalid_type in invalid_types:
        with pytest.raises(TypeError):
            mask_account_card(invalid_type)


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
