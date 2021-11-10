from random import randint
from pprint import pprint

# Создание квадратной матрицы с рандомными значениями
matrix = [[randint(0, 10) for n in range(0, 3)] for m in range(0, 3)]
pprint(matrix)

# Поиск и замена
index = 0
for i in matrix:
    max_value = max(i)
    i[index] = max_value
    index += 1
pprint(matrix)