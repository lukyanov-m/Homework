from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Принимает тип и номер карты или счета, а возвращает тип и замаскированный номер"""
    if card_or_account[-20:].isdigit():
        return f"Счет {get_mask_account(card_or_account[-20:])}"
    else:
        return f"{card_or_account[:-16]}{get_mask_card_number(card_or_account[-16:])}"

print(mask_account_card("Счет 35383033474447895560"))