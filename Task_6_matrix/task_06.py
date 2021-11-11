# Создать матрицу случайных чисел от a до b, размерность матрицы n*m

from random import randint
from copy import deepcopy

a = 1
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

# Найти индекс колонки с максимальной суммой элементов

index_col_max_arr = []
j = 0
len_matrix = len(matrix)
len_of_element = len(matrix[0])
while j < len_of_element:
    i = 0
    sum_of_elements = 0
    while i < len_matrix:
        sum_of_elements += matrix[i][j]
        i += 1
    index_col_max_arr.append(sum_of_elements)
    j += 1
max_col_sum = max(index_col_max_arr)
max_col_index = index_col_max_arr.index(max_col_sum)
print(index_col_max_arr, max_col_index)

# Найти индекс ряда с минимальной суммой элементов

index_row_min_arr = []

for i in matrix:
    index_row_sum = 0
    for j in i:
        index_row_sum += j
    index_row_min_arr.append(index_row_sum)
min_sum = min(index_row_min_arr)
min_index_sum = index_row_min_arr.index(min_sum)
print(index_row_min_arr, min_index_sum)

# Найти индекс колонки с минимальной суммой элементов

index_col_min_arr = []

for i, k in enumerate(matrix):
    min_sum_of_elements = 0
    for j, r in enumerate(k):
        min_sum_of_elements += matrix[j][i]
    index_col_min_arr.append(min_sum_of_elements)
min_col_sum = min(index_col_min_arr)
min_col_sum_index = index_col_min_arr.index(min_col_sum)
print(index_col_min_arr, min_col_sum_index)

# Обнулить все элементы выше главной диагонали

new_matrix_zero_above = deepcopy(matrix)
starter_point = 1
for i, k in enumerate(new_matrix_zero_above):
    j = starter_point
    len_of_k = len(k)
    while j < len_of_k:
        new_matrix_zero_above[i][j] = 0
        j += 1
    starter_point += 1
print(new_matrix_zero_above)

# Обнулить все элементы ниже главной диагонали

new_matrix_zero_behind = deepcopy(matrix)
ending_point = 0
for i, k in enumerate(new_matrix_zero_behind):
    for j, v in enumerate(k):
        if j < ending_point:
            new_matrix_zero_behind[i][j] = 0
    ending_point += 1
print(new_matrix_zero_behind)

