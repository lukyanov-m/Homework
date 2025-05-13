import json
from json import JSONDecodeError
from typing import Any, Dict, List


def get_financial_transaction_data(path: str) -> List[Dict[str, Any]]:
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


print(get_financial_transaction_data("../data/operations.json"))
