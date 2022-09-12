# -*- coding: utf-8 -*-
# Методы классов
class Point:
    "Класс для представления координат на плоскости"
    color = 'red'
    circle = 2

    def set_coords(self, x, y):  # Параметр self ссылается на экземпляр из которого был вызван метод
        print("вызов метода set_coords "  + str(self))
        # Создадим в экземпляре класса два свойства (если таких свойств ещё нет).
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

print(Point.set_coords)
# Point.set_coords()

pt = Point()  # Создаем экземпляр класса
print(pt.set_coords)
pt.set_coords(2, 3)  # Аргумент self передается автоматически
Point.set_coords(pt, 2, 3)

print(hasattr(Point, 'x'))  # У класса нет аргумента х
print(hasattr(pt, 'x'))  # У экземпляра есть аргумент х
print(pt.get_coords())

f = getattr(pt, 'get_coords')
print(f())
