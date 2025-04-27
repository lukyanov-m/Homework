from typing import Any, Dict, Iterator


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


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Функция генератор принимает диапазон чисел в котором создает номера в формате XXXX XXXX XXXX XXXX
    """
    if start > 0 and len(str(stop)) <= 16:
        for number in range(start, stop):
            card_number = str(number).zfill(16)
            format_card_number = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
            yield format_card_number
    else:
        yield "Выход за рамки диапазона"
        yield "Поменяйте параметры, они должны быть положительными и иметь не более 16 цифр"
