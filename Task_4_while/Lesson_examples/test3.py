n = int(input('Введи начальное значение'))
m = int(input('Введи конечное значение'))
t = int(input('Введи шаг'))
new_list = [x for x in range(n, m, t)]
print(new_list)

arr = []
while n <= m:
    arr.append(n)
    n += t
print(arr)
