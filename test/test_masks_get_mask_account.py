import pytest
from src.masks import get_mask_account


@pytest.fixture
def account_data():
    """Тестовые данные для проверки маскирования счета"""
    return [
        (12345678901234567890, "**7890"),   # стандартный номер
        ("98765432109876543210", "**3210"), # строка
        (1234, "**1234"),                   # короткий номер
        (567890, "**7890"),                 # номер средней длины
        ("", ""),                           # пустая строка
    ]


def test_get_mask_account(account_data):
    """Проверка маскирования номера счета"""
    for account, expected in account_data:
        assert get_mask_account(account) == expected