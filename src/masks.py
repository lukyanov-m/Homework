def get_mask_card_number(card_number: str) -> str:
    """Функция разбивает номер карты по блокам и скрывает часть этого номера"""
    str_card_number = str(card_number)
    if not isinstance(card_number, str):
        raise TypeError("Неверный тип данных")
    elif not card_number.isdigit() or len(str_card_number) != 16:
        raise ValueError("Не корректный номер карты")

    block1 = str_card_number[:4]
    block2 = str_card_number[4:6] + "**"
    block3 = "****"
    block4 = str_card_number[12:]
    return f"{block1} {block2} {block3} {block4}"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает последние четыре цифры номера счета"""
    if not isinstance(account_number, str):
        raise TypeError("Неверный тип данных")
    elif not account_number.isdigit() or len(account_number) != 20:
        raise ValueError("Не корректный номер счета")
    return f"**{account_number[-4:]}"
