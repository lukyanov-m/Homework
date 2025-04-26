from typing import Iterator


def filter_by_currency(list_dict: list, currency: str) -> Iterator[dict]:
    """
    Функция генератор принимает список словарей и необходимую валюту, возвращает только словари с указанной валютой
    """
    for operation in list_dict:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation
