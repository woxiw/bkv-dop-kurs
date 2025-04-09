def filter_greater_than(arr: list[int], threshold: int) -> list[int]:
    # Используем списковое включение для фильтрации элементов
    return [x for x in arr if x > threshold]

# Пример использования
print(filter_greater_than([1, 5, 8, 3, 10], 5))  # Вывод: [8, 10]
