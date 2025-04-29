import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(list_transactions):
    generator_filter_by_currency_usd = filter_by_currency(list_transactions, "USD")
    assert next(generator_filter_by_currency_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator_filter_by_currency_usd) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_empty_generator():
    empty_generator = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        raise next(empty_generator)


# @pytest.mark.parametrize
def test_transaction_descriptions(list_transactions):
    generator_transaction_descriptions = transaction_descriptions(list_transactions)
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (5, 7, ["0000 0000 0000 0005", "0000 0000 0000 0006"]),
        (2222333344445555, 2222333344445557, ["2222 3333 4444 5555", "2222 3333 4444 5556"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    generator_card_number_list = list(card_number_generator(start, stop))
    assert generator_card_number_list == expected

    generator_card_number = card_number_generator(1, 3)
    assert next(generator_card_number) == "0000 0000 0000 0001"
    assert next(generator_card_number) == "0000 0000 0000 0002"
    with pytest.raises(StopIteration):
        raise next(generator_card_number)
