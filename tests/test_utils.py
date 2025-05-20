import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_financial_transaction_data, get_transaction_amount


@pytest.mark.parametrize(
    "input_data,expected", [(json.dumps([{"id": 1}]), [{"id": 1}]), ("", []), ("not a json", []), (None, [])]
)
def test_get_financial_transaction_data(input_data, expected):
    with (
        patch("builtins.open", mock_open(read_data=input_data))
        if input_data is not None
        else patch("builtins.open", side_effect=FileNotFoundError)
    ):
        assert get_financial_transaction_data("test.json") == expected


@pytest.mark.parametrize("input_data,expected", [("1", None), (1, None)])
def test_get_transaction_amount(input_data, expected):
    assert get_transaction_amount(input_data) == expected
