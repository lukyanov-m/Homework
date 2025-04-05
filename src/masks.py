def get_mask_card_number(card_number: [int | str]) -> str:
    """Функция разбивает номер карты по блокам и скрывает часть этого номера"""
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        return "Не корректный номер карты"
    block1 = str_card_number[:4]
    block2 = str_card_number[4:6] + "**"
    block3 = "****"
    block4 = str_card_number[12:]
    return f"{block1} {block2} {block3} {block4}"


def get_mask_account(account_number: [int | str]) -> str:
    """Функция возвращает последние четыре цифры номера счета"""
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        return "Не корректный номер счета"
    return "**" + str_account_number[-4:]
