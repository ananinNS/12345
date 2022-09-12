# -*- coding: utf-8 -*-
# Статические методы и методы класса
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @staticmethod
    def norm2(x, y):  # Сервисная функция (нет cls и self). Данный метод не имеет доступ не к атрибутам класса, не к атрибутом его экземпляров.
        return x*x + y*y

    @classmethod
    def validate(cls, arg):  # В методе класса будет параметр cls, чтобы работать с атрибутами класса, но не может обращаться к атрибутам класса
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(1, 2)
print(Vector.validate(5))
print(Vector.norm2(5, 6))
res = v.get_coord()
print(res)
