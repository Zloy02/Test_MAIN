list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей,
# где на первом месте стоит индекс, а затем значение
# [(0, -5), (1, 2), (2, 4), ...]
for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")
