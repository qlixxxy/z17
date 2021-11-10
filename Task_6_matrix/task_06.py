# Создать матрицу случайных чисел от a до b, размерность матрицы n*m

from random import randint

a = 0
b = 10
n = 5
m = 5
matrix = [[randint(a, b) for i in range (0, m)] for x in range(0, n)]
print(matrix)

# Найти максимальный элемент матрицы

max_el = 0

for i in matrix:
    for j in i:
        if j > max_el:
            max_el = j
print(max_el)

# Найти минимальный элемент матрицы

min_el = 0

for i in matrix:
    for j in i:
        if j < min_el:
            min_el = j
print(min_el)

# Найти сумму всех элементов матрицы

sum = 0

for i in matrix:
    for j in i:
        sum += j
print(sum)

# Найти индекс ряда с максимальной суммой элементов

index_row_max_arr = []

for i in matrix:
    index_row_sum = 0
    for j in i:
        index_row_sum += j
    index_row_max_arr.append(index_row_sum)
max_sum = max(index_row_max_arr)
max_index_sum = index_row_max_arr.index(max_sum)
print(index_row_max_arr, max_index_sum)