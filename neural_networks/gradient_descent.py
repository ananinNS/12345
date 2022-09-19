# -*- coding: utf-8 -*-
# Реализован алгоритм градиентного спуску.

str = "Привет мир"

for v in str:
    print(v, end=", ")

class MyClass:
    a1 = "Привет"
    a2 = 2


b = MyClass()

print(MyClass.a1)
MyClass.a1 = "111141"
b.a1 = "7777"
b.ss = 123
print(b.a1, MyClass.a1, b.ss)


def gene(start_value):
    start_value += 1
    yield start_value


b = gene(2)

print(type(b))
print(b.__next__())
