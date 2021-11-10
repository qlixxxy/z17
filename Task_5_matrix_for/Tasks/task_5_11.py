from random import randint

n = int(input('Введи размерность n x n'))

matrix = [[randint(0, 10) for i in range(0, n)] for j in range(0, n)]

sum = 0
i = 0
j = 1
while i < len(matrix):
    j = i + 1
    while j < len(matrix[i]):
        sum += matrix[i][j]
        j += 1
    i += 1

print(matrix, sum)