# Выражения генераторы.

# Создадим генератор чисел. Создается в круглых скобках.
a = (x ** 2 for x in range(6)) # В a ссылка на генератор.
print(a)

# Генератор тоже является итератором и из него можно получать значения функцией next. Перебрать можно только 1 раз.
print(next(a))
print(next(a))
print(next(a))

# Некоторым стандартным функциям можно передавать генераторы в качестве параметров.
a = (x ** 2 for x in range(6))
print(list(a)) # Генератор преобразуем в список.
a = (x ** 2 for x in range(6))
print(set(a)) # Генератор преобразуем в множество.
a = (x ** 2 for x in range(6))
print(max(a))
a = (x ** 2 for x in range(6))
print(sum(a))

# Генераторы используют потому что они не хранят в памяти сразу все значения, а генерируют их по мере необходимости.