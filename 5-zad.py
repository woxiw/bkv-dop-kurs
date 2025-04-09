def convert_to_12_hour_format(hours: int, minutes: int) -> str:
    """
    Конвертирует время из 24-часового формата в 12-часовой с AM/PM
    """
    # Проверка корректности ввода
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError("Некорректное время")
    
    # Определение AM/PM и конвертация часов
    period = 'AM' if hours < 12 else 'PM'
    converted_hour = hours % 12
    if converted_hour == 0:  # 0 часов становится 12
        converted_hour = 12
    
    # Форматирование строки с ведущим нулём для минут
    return f"{converted_hour}:{minutes:02d} {period}"

# Примеры использования
print(convert_to_12_hour_format(14, 30))  # 2:30 PM
print(convert_to_12_hour_format(0, 45))   # 12:45 AM
print(convert_to_12_hour_format(12, 0))   # 12:00 PM
print(convert_to_12_hour_format(23, 5))   # 11:05 PM
