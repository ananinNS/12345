# -*- coding: utf-8 -*-
# Функции all() и any()
# a = [True, True, True, True]
a = [0, 1, 2.5, "", "python", [], [1, 2], {}]
print(all(a))  # Если все значения True, то вернет True
# Прежде чем выполняется функция all все значения приводятся к булевому типу. Пустые строки, списки - False

# any() - если какое то значение True, то будет True

# Определение есть ли выигрышная позиция в крестики нолики
P = ["x", "x", "0", "0", "x", "0", "x", "x", "x"]

def true_x(a):
    return a == "x"


# По строчкам
row_1 = all(map(true_x, P[:3]))  # Стоят ли в строке 3 крестика подряд.
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))

# По столбцам
col_1 = all(map(true_x, P[::3]))  # Стоят ли в строке 3 крестика подряд.
col_2 = all(map(true_x, P[1::3]))
col_3 = all(map(true_x, P[2::3]))

print(row_1, row_2, row_3)
print(col_1, col_2, col_3)
