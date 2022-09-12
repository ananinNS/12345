# Словари
d = {"house": "дом", "car": "дом",
     "tree": "дерево", "road": "дорога",
     "river": "река"}

print(d)
print("house")
# Ещё один способ создать словарь
d2 = dict(one = 1, two = 2, three = "3", four = 4)
print(d2)
d2["five"] = 5# Добавляем новый ключ-значение
print(d2)
d2["five"] = -5 # Изменяем значение по ключу
print(d2)
del d2["five"] # Удаляем ключ - значение
print(d2)
print("five" in d2)