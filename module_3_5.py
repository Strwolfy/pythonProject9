def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    first = int(str_number[0])  # Получаем первую цифру числа

    # Если первая цифра 0, то пропускаем её
    if first == 0:
        return get_multiplied_digits(int(str_number[1:])) if len(str_number) > 1 else 1

    # Если длина числа больше 1, рекурсивно вызываем функцию для оставшейся части
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first  # Возвращаем первую цифру, если больше цифр нет


# Пример использования
result = get_multiplied_digits(42220)
print(result)