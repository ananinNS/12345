# -*- coding: utf-8 -*-
# Магический метод __new__() вызывается перед созданием объекта класса.
class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))  # cls ссылается на Point
        return super().__new__(cls)  # Обязательно должны вернуть адрес нового объекта.
        # Все классы наследуются от базового класса

    def __init__(self, x=0, y=0):  # self ссылается на созданный экземпляр
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt)


# Паттерн Singleton
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        print("чтение данных из БД")

    def write(self, data):
        print(f"запись данных в БД")


db = DataBase("root", "1234", 80)
db2 = DataBase("root2", "5678", 40)
print(id(db), id(db2))
#  Есть недостаток при попытке создать второй объект, объект был не создан, но параметры его записаны в свойства
