from masks import get_mask_account, get_mask_card_number

def mask_account_card(card: str) -> str:
    card_list = card.split(" ")
    if len(card_list[-1]) == 16:
        masks_card = get_mask_card_number(card_list[-1])
    else:
        masks_card = get_mask_account(card_list[-1])

    return masks_card


