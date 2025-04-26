from typing import Dict, Iterator


def filter_by_currency(list_dict: list[Dict], currency: str) -> Iterator[dict]:
    """
    Функция генератор принимает список словарей с транзакциями и необходимую валюту,
    возвращает только словари с указанной валютой.
    """
    for operation in list_dict:
        if operation.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield operation


def transaction_descriptions(list_dict: list) -> Iterator[str]:
    """
    Генератор принимает список словарей с транзакциями, возвращает только описание транзакции.
    """
    for operation in list_dict:
        yield operation.get("description")
