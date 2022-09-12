# -*- coding: utf-8 -*-
# Режимы доступа (инкапуляция)
# Атрибут без подчеркивания, значит доступ публичный
# одно подчеркивание protected Одно нижнее подчеркивание только сигнализирует, но не мешает использовать
# два подчеркивания перед именем private
#
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):  # Приватный метод
        return type(x) in (int, float)

    def set_coord(self, x, y):
        "Сеттер"
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Кординаты должны быть числами")

    def get_coord(self):
        "Геттер"
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(100, 200)
print(pt.get_coord())

# Можно использовать библиотеку accessify чтобы сделать атрибуты класса приватными
# from accessify import private, protected Более сильная защита, чем два подчеркивания.
