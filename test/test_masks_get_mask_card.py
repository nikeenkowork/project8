from src.masks import get_mask_card_number

def test_get_mask_card_number():
    """Проверка правильности маскирования номера карты"""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_get_mask_card_number_mastercard():
    """Проверка маскирования другого номера карты"""
    assert get_mask_card_number("5555555555554444") == "5555 55** **** 4444"


def test_no_card_number_text():
    """Строка без номера карты"""
    assert get_mask_card_number("Visa Classic") == "Visa Classic"


def test_empty_string():
    """Пустая строка"""
    assert get_mask_card_number("") == ""


def test_short_number():
    """Граничный случай — номер меньше 16 цифр"""
    assert get_mask_card_number("12345678") == "12345678"