from .masks import get_mask_account, get_mask_card_number

"""Функция которая умеет обрабатывать информацию как о картах, так и о счетах."""


def mask_account_card(card: str) -> str:
    card_list = card.split(" ")
    if len(card_list[-1]) == 16:
        masks_card = f"{" ".join(card_list[:-1])} {get_mask_card_number(card_list[-1])}"
    else:
        masks_card = f"{" ".join(card_list[:-1])} {get_mask_account(card_list[-1])}"

    return masks_card


"""Функция которая обрабатывает дату"""


def get_date(str_data: str) -> str:
    data_new = f"{str_data[8:10]}.{str_data[5:7]}.{str_data[:4]}"

    return data_new
