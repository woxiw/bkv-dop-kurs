def find_min_max(arr: list[int]) -> tuple[int, int] | None:
    """
    Находит минимальный и максимальный элементы в массиве.
    Возвращает кортеж (min, max) или None для пустого массива.
    """
    if not arr:
        return None
    
    min_val = max_val = arr[0]
    
    # Оптимизированный однопроходный поиск
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return (min_val, max_val)

# Примеры использования
print(find_min_max([3, 1, 4, 1, 5, 9, 2]))  # (1, 9)
print(find_min_max([-10, 0, 15, 7]))       # (-10, 15)
print(find_min_max([]))                     # None
