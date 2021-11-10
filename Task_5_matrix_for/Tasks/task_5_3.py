from pprint import pprint
arr = []
dict = {}

# Нахождение суммы делителей для числа и занесение их в словарь по шаблону {число: сумма делителей}
for i in range(200, 301):
    n = 1
    sum = 0
    while n < i:
        if i % n == 0:
            sum += n
        n += 1
    dict[i] = sum

# Создание уникальных значений 
values_set = set(dict.values())

# Создание пар ключей, у который одинаковая сумма общих делителей
for value in values_set:
    inner_arr = []
    for key in dict:
        if dict[key] == value:
            inner_arr.append(key)
    arr.append(inner_arr)
pprint(arr)

