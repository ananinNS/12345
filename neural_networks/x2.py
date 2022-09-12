# -*- coding: utf-8 -*-
# Генератор для функции x в квадрате и её производной.

def get_generator_x2(x0, h, step=0):
    """
    Получить генератор для функции x^2
    :param x0: Начальное значение, с которого начинаем генерировать
    :param h: Шаг генерации
    :param step: Кол-во генераций, если значение равно 0, то генерарация бесконечная
    :return:  генератор для функции x^2
    """
    infinitely = step == 0
    while infinitely or step > 0:
        res = x0 * x0
        yield res
        x0 += h
        if step > 0:
            step -= 1


def get_generator_x2_derivative(x0, h, step=0):
    """
    Получить генератор для производной функции x^2
    :param x0: Начальное значение, с которого начинаем генерировать
    :param h: Шаг генерации
    :param step: Кол-во генераций, если значение равно 0, то генерарация бесконечная
    :return:  генератор для производной функции x^2
    """
    infinitely = step == 0
    while infinitely or step > 0:
        res = 2 * x0
        yield res
        x0 += h
        if step > 0:
            step -= 1


# Проверка генератора x^2 (get_generator_x2)
g = get_generator_x2(-10, 1, 21)
for v in g:
    print(v, end=", ")
print()

# Проверка генератора производной x^2 (get_generator_x2_derivative)
g = get_generator_x2_derivative(-10, 1, 21)
for v in g:
    print(v, end=", ")
