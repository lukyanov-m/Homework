from src.masks import get_mask_account, get_mask_card_number

number_card = get_mask_card_number("2568475325984528")
number_account = get_mask_account(15478562456985215489)

print("Номер карты: " + number_card)
print("Номер счета: " + number_account)
