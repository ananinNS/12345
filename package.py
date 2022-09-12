# Пакеты. Пакет - специальным образом организованный подкаталог с набором модулей, как правило, решающих сходные задачи.
import courses

print(dir(courses))

courses.python.get_python()

courses.get_java() # Импорт без пространства имен java