import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/Mishanya/PycharmProjects/Bank/.env")

ERD_API_KEY = os.getenv("ERD_API_KEY")


def get_currency_conversion(currency_to: str, currency_from: str, amount: float) -> float:
    """Функция конвертации валюты"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

    headers = {"apikey": ERD_API_KEY}

    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    result = response.json()

    if status_code != 200:
        raise ValueError("Не удалось получить курс валюты")
    else:
        return result["result"]
