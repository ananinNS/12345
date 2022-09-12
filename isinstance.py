# -*- coding: utf-8 -*-
# Функция isinstance соответсвие объекта типу данных
a = 5
print(isinstance(a, int))
print(isinstance(a, float))
b = True
print(isinstance(b, bool))
print(isinstance(b, int)) # Тоже будет True, так как тип bool наследуется от типа int
# Делает проверку с учетом наследования.
# Можно сделать строгую проверку.
print(type(b) == bool)
print(type(b) == int)  # False так как строгая проверка.
# Можно сделать ещё так
print(type(b) is bool)
print(type(b) is int)
# Проверка на несколько типов данных
print(type(b) in (bool, float, str))

# Посчитаем сумму только вещественных чисел
data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])
s = sum(filter(lambda x: type(x) is float, data))
print(s)

# Сумма целочисленных значений
s = sum(filter(lambda x: type(x) is int, data))
print(s)

# Множественные проверки
a = 5.5
print(isinstance(a, (float, int)))  # True если принадлежит какомуто из типов.

