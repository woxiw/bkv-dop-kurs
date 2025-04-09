def count_unique_chars(s: str) -> int:
    # Используем множество для хранения уникальных символов
    unique_chars = set()
    
    # Перебираем каждый символ в строке и добавляем в множество
    for char in s:
        unique_chars.add(char)
    
    # Возвращаем размер множества (количество уникальных символов)
    return len(unique_chars)

# Пример использования
print(count_unique_chars("hello"))  # Вывод: 4
