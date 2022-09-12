# В данном файле указывает, что следует импортировать в данном пакете.
import courses.python
import courses.html
from .php import get_php, get_mysql  # Относительный импорт.
from courses.java import * # Можно импортировать без пространства имен java
from .doc import * # Импорт другого пакета.
NAME = "package courses"
