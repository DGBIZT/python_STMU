from src.masks import get_mask_account, get_mask_card_number

# Маскировка номера банковской карты

number_card = get_mask_card_number("7000792289606361")
print(number_card)

# Маскировка номера банковского счета
account_number = get_mask_account("73654108430135874305")
print(account_number)
