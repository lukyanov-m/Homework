import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import get_currency_conversion

load_dotenv("C:/Users/Mishanya/PycharmProjects/Bank/.env")

ERD_API_KEY = os.getenv("ERD_API_KEY")


@patch("requests.request")
def test_get_currency_conversion_api_error(mock_request):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "Invalid currency"}
    mock_request.return_value = mock_response

    with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
        get_currency_conversion("RUB", "USD", 100)


@patch("requests.request")
def test_get_currency_conversion_invalid_json(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_request.return_value = mock_response

    with pytest.raises(ValueError):
        get_currency_conversion("RUB", "USD", 100)


@patch("requests.request")
def test_get_currency_conversion(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 1}
    mock_request.return_value = mock_response
    assert get_currency_conversion("RUB", "USD", 10) == 1
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10",
        headers={"apikey": ERD_API_KEY},
    )
