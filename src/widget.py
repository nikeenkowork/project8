import re


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета.
    """

    # Если это счёт (20 цифр после слова "Счет")
    account_pattern = r"(Счет)\s+(\d{16,20})"
    # r " ... " Это сырая строка (raw string) нужна, чтобы \s и \d воспринимались как специальные символы
    # \d означает цифра
    # \s означает пробельный символ (пробел, таб, перенос строки)
    # + означает один или больше символов

    # Если это карта (16 цифр)
    card_pattern = r"(.+?)\s+(\d{16})"
    # . = любой символ
    # ? = элемент Regex (regular expression - специальный шаблон для поиска и обработки текста)

    # Проверяем счёт
    account_match = re.search(account_pattern, data)
    if account_match:
        name = account_match.group(1)  # группа 1 — “название карты”
        number = account_match.group(2)  # группа 2 — номер карты
        return f"{name} **{number[-4:]}"

    # Проверяем карту
    card_match = re.search(card_pattern, data)
    if card_match:
        name = card_match.group(1)
        number = card_match.group(2)
        masked = f"**** **** **** {number[-4:]}"
        return f"{name} {masked}"

    return "Некорректные данные"


def get_date(date_str: str) -> str:
    """Принимает строку с датой в формате "2024-03-11Т02:26:18.671407"
    и возвращает строку в формате "11.03.2024".
    """
    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:10]

    return f"{day}.{month}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))
