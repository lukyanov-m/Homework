from typing import Dict, Iterator, Any


def filter_by_currency(list_dict: list[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Функция генератор принимает список словарей с транзакциями и необходимую валюту,
    возвращает только словари с указанной валютой.
    """
    for operation in list_dict:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation


def transaction_descriptions(list_dict: list[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор принимает список словарей с транзакциями, возвращает только описание транзакции.
    """
    for operation in list_dict:
        yield operation["description"]


def card_number_generator():
    pass
