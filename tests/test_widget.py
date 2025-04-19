import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305")
    ]
)
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


