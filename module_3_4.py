def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для корректного сравнения
    root_word_lower = root_word.lower()

    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержится ли root_word в слове или слово в root_word
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем список с подходящими словами
    return same_words


# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результата на экран
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']