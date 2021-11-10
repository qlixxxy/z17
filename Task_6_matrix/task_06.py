# Создать матрицу случайных чисел от a до b, размерность матрицы n*m

from random import randint

a = 0
b = 10
n = 5
m = 5
matrix = [[randint(a, b) for i in range (0, m)] for x in range(0, n)]
print(matrix)