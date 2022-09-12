# Работа с файлами.
# Чтение данных из файла.

file = open("my_file.txt",
            encoding='utf-8')  # Если файл находится тамже, где и исполняемый файл. Можем только считывать файл.

# Пути лучше прописывать вот так: "d:/app/my_file.txt". Так будет работать и в Windows и в Linux.

# print(file.read(4)) # Читаем 4 символа c файловой позиции.
print(file.read())
# file.seek() - метод для управления файловой позиции.
# file.tell() - возвращает текущую файловую позицию. Файловая позиция указывает не номер символа, а номер байта. В utf-8 два байта на символ.
# file.readline() - читает строчку из файла.

# for line in file:  # Перебираем файл по строчно.
#    print(line, end="")

# s = file.readlines() # Получаем список из строк.
file.close()  # Закрываем файл.
# Обработка исключения FileNotFoundError
try:
#    file = open("my_file.txt", encoding='utf-8')
    # Менеджер контекста, замена блока try - finally
    with open("my_file.txt", encoding='utf-8') as file:
        s = file.readlines()
        print(s)
    # try:
    #     s = file.readlines()
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print("Файл с таким именем не существует")
except:
    print("Неизвестная ошибка при работе с файлом")
finally:
    print(file.closed)# Проверяем закрыт ли файл.

#file.close()  # Закрываем файл.
