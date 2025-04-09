class Stack:
    def init(self, size=10):
        # Инициализация стека с фиксированным размером
        self.size = size
        self.stack = [None] * size  # Создаем массив фиксированного размера
        self.top_index = -1  # Индекс вершины стека (-1 означает пустой стек)
    
    def is_empty(self):
        # Проверка, пуст ли стек
        return self.top_index == -1
    
    def push(self, value):
        # Добавление элемента в стек
        if self.top_index >= self.size - 1:
            print("Ошибка: Стек переполнен")
            return
        
        self.top_index += 1
        self.stack[self.top_index] = value
    
    def pop(self):
        # Удаление элемента из стека и возвращение его значения
        if self.is_empty():
            print("Ошибка: Стек пуст")
            return None
        
        value = self.stack[self.top_index]
        self.top_index -= 1
        return value
    
    def top(self):
        # Возвращение элемента на вершине стека без удаления
        if self.is_empty():
            print("Ошибка: Стек пуст")
            return None
        
        return self.stack[self.top_index]


# Пример использования
if name == "main":
    # Создаем стек размером 5 элементов
    stack = Stack(5)
    print("Создан стек размером 5 элементов")
    
    # Добавляем элементы
    print("\nДобавляем элементы в стек:")
    stack.push(10)
    print("Добавлен элемент: 10")
    stack.push(20)
    print("Добавлен элемент: 20")
    stack.push(30)
    print("Добавлен элемент: 30")
    
    # Проверяем верхний элемент
    print(f"\nВерхний элемент: {stack.top()}")
    
    # Удаляем элемент
    popped = stack.pop()
    print(f"\nУдален элемент: {popped}")
    
    # Проверяем верхний элемент после удаления
    print(f"Новый верхний элемент: {stack.top()}")
    
    # Проверка переполнения
    print("\nПроверка на переполнение:")
    stack.push(40)
    print("Добавлен элемент: 40")
    stack.push(50)
    print("Добавлен элемент: 50")
    stack.push(60)  # Стек уже содержит 4 элемента, это будет 5-й (последний)
    print("Добавлен элемент: 60")
    stack.push(70)  # Должно появиться сообщение о переполнении
    
    # Удаляем все элементы
    print("\nУдаляем все элементы из стека:")
    while not stack.is_empty():
        print(f"Удален элемент: {stack.pop()}")
    
    # Пытаемся удалить элемент из пустого стека
    print("\nПытаемся удалить элемент из пустого стека:")
    stack.pop()  # Должно появиться сообщение об ошибке
