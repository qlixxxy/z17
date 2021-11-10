m = int(input('Введите стартовое значение'))
n = int(input('Введите конечное значение'))
range_values = range(m, n)
for i in range_values:
    empty_arr = []
    x = 2
    while x < i:
        if i % x == 0:
            empty_arr.append(str(x))
        x += 1
    string_arr = ' '.join(empty_arr)
    print(f'{i}: {string_arr}')
