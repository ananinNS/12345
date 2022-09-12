# -*- coding: utf-8 -*-
class Point:
    "Класс для представления координат на плоскости"
    color = 'red'
    circle = 2


print(Point.color, Point.circle, sep=", ")

print(Point.__dict__)  # Все отребуты класса

a = Point()  # Создание экземпляра класса.
b = Point()  # Создаем ещё один объект
print(id(a), id(b))
print(id(a.color), id(b.color))  # Атрибуты общие для двух объектов.
# Объекты a и b не содержат атребутов
print(a.__dict__, b.__dict__)  # Объекты a и b не содержат атребутов

a.color = 'black'  # Теперь объект a имеет собственную переменную color
print(id(a.color), id(b.color), id(Point.color))
print(a.__dict__)

# Создание в классе нового поля
Point.type_pt = 'disk'
print(Point.__dict__)
# Новый аргумент можно создать ещё так
setattr(Point, 'prop', 1)
print(Point.__dict__)

# Обращение к несуществующему атребуту класса
print(getattr(Point, 'a', False))  # Функция возвращает False, если атрибута нет.

# Удаление атрибута
del Point.prop
# delattr(Point, 'prop')  # Или так.
# del a.circle # Удалить нельзя так как атрибут присутствует в классе Point
del a.color  # После удаления атрибута объект будет ссылаться на атрибут класса.

# Не зависимые от класса атрибуты в объектах
a.x = 1
a.y = 2
b.x = 10
b.y = 20

# Описание класса
print(Point.__doc__)
