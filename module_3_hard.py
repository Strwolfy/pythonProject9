def calculate_structure_sum(data):
    total_sum = 0

    # Если data - список, кортеж или множество, рекурсивно перебираем его элементы
    if isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)

    # Если data - словарь, рекурсивно перебираем как ключи, так и значения
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Обрабатываем ключи
            total_sum += calculate_structure_sum(value)  # Обрабатываем значения

    # Если data - строка, добавляем её длину
    elif isinstance(data, str):
        total_sum += len(data)

    # Если data - число (целое или вещественное), добавляем его к сумме
    elif isinstance(data, (int, float)):
        total_sum += data

    # Возвращаем итоговую сумму
    return total_sum

# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции и вывод результата
result = calculate_structure_sum(data_structure)
print(result)
