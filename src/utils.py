import json
from json import JSONDecodeError
from pathlib import Path
from typing import Any, Dict, List, Union

from src.external_api import get_currency_conversion


def get_financial_transaction_data(path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Функция принимает путь до json файла, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as bank_fail:
            try:
                bank_data = json.load(bank_fail)
            except JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

    return bank_data


def get_transaction_amount(transaction: int) -> float:
    """функция, принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли"""

    list_data = get_financial_transaction_data("../data/operations.json")

    for data in list_data:
        if data.get("id") != transaction:
            continue
        if data["operationAmount"]["currency"]["code"] == "RUB":
            return data["operationAmount"]["amount"]
        else:
            return get_currency_conversion(
                "RUB", data["operationAmount"]["currency"]["code"], data["operationAmount"]["amount"]
            )
