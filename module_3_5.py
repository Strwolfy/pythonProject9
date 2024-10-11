def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Извлекаем первую цифру и преобразуем её обратно в число
    first = int(str_number[0])

    # Если в числе осталась только одна цифра, возвращаем её
    if len(str_number) == 1:
        return first

    # Рекурсивный вызов функции для оставшихся цифр числа
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)  # Ожидаемый результат: 24
