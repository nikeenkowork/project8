def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскирует номер банковской карты.
    """
    bank_card = str(card_number)
    return f"{s[:4]} {s[4:6]}** **** {s[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Функция маскирует номер банковского счета.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
