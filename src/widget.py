from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Принимает тип и номер карты или счета, а возвращает тип и замаскированный номер"""
    if card_or_account[-20:].isdigit():
        return f"Счет {get_mask_account(card_or_account[-20:])}"
    else:
        return f"{card_or_account[:-16]}{get_mask_card_number(card_or_account[-16:])}"


def get_date(date_and_time: str) -> str:
    """Принимает строку с датой и временем ГГГГ-ММ-ДД+время, возвращает дату в формате ДД.ММ.ГГГГ"""
    list_date = date_and_time[:10].split("-")
    return f"{list_date[2]}.{list_date[1]}.{list_date[0]}"
