# -*- coding: utf-8 -*-
# Функция zip - осуществляет перебор нескольких итерируемых объектов
# пока не дойдет до самой короткой.
# Объект zip также является итератором.
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"
z = zip(a, b, c)
print(z)
print(next(z))
print(next(z))
for x in z:
    print(x)

# Можно сразу распокавать кортеж
z = zip(a, b, c)
for v1, v2, v3 in z:
    print(v1, v2, v3)

# Можно распокавать кортежи (распаковка итератора)
z1, z2, z3, z4 = zip(a, b, c) # Нужно заранее знать кол-во.
print(z1, z2, z3, z4)

