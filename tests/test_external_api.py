import pytest
from unittest.mock import patch, Mock
from requests.exceptions import RequestException

from src.external_api import get_currency_conversion


# Тест для ошибки API (не 200 статус)
@patch('requests.request')
def test_get_currency_conversion_api_error(mock_request):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "Invalid currency"}
    mock_request.return_value = mock_response

    with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
        get_currency_conversion("RUB", "USD", 100)


@patch('requests.request')
def test_get_currency_conversion_invalid_json(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_request.return_value = mock_response

    with pytest.raises(ValueError):
        get_currency_conversion("RUB", "USD", 100)

# Параметризованный тест для разных валют и сумм
@pytest.mark.parametrize("from_curr,to_curr,amount", [
    ("USD", "RUB", 100),
    ("EUR", "USD", 50),
    ("GBP", "EUR", 75),
])
@patch('requests.request')
def test_different_currencies(mock_request, from_curr, to_curr, amount):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": from_curr, "to": to_curr, "amount": amount},
        "result": amount * 75  # Произвольный курс для теста
    }
    mock_request.return_value = mock_response

    result = get_currency_conversion(to_curr, from_curr, amount)
    assert result["query"]["from"] == from_curr
    assert result["query"]["to"] == to_curr
    assert result["query"]["amount"] == amount