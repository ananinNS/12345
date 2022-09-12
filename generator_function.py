
def get_list():
    for x in [1, 2, 3, 4]:
        yield x # function generator. Freez state function for next call.


a = get_list()
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
a = get_list()
for x in a:
    print(x)