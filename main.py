from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

# Маскировка номера банковской карты

number_card = get_mask_card_number("7000792289606361")
print(number_card)

# Маскировка номера банковского счета
account_number = get_mask_account("73654108430135874305")
print(account_number)

# Функция которая умеет обрабатывать информацию как о картах, так и о счетах
mask_ac_card = mask_account_card("Счет 73654108430135874305")
print(mask_ac_card)

# Функция которая принимает на вход строку с датой в форме "2024-03-11T02:26:18.671407"
# и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
data_new = get_date("2024-03-11T02:26:18.671407")
print(data_new)

print("Hello Git!")