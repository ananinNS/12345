# Битовые операции
# Оператор НЕ
a = 121
print(bin(a))
print(bin(~a))

# Операция И
flags = 5
mask = 4
res = flags & mask
print(res)

# Операция ИЛИ
flags = 8
mask = 5
res = flags | mask
print(res)

# Исключающая ИЛИ
flags = 9
mask = 1
res = flags ^ mask
print(res)

# Самый высокий приоритет у операции НЕ, потом у И далее у или и исключающее или.

# Сдвиговые операторы
x = 160
print(bin(x))
print(bin(x >> 1))
print(bin(x << 1))
