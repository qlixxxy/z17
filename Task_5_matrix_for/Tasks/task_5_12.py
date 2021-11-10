from random import randint

# Создание матрицы 3х4 с рандомными значениями

matrix = [[randint(0, 10) for k in range(0, 4)] for v in range(0, 3)]

# Присвоение переменных

A = 2
sum = 0
i = 0
j = 0
counter_of_iterations = 0
length = len(matrix)
length_of_element = len(matrix[i])

# Проход по циклу с условием и при counter_of_iterations <= 9 

while j < length_of_element:
    i = 0
    if matrix[i][j] > A and counter_of_iterations < 9:
        while i < length:
            sum += matrix[i][j]
            i += 1
            counter_of_iterations += 1
    j += 1
print(matrix, sum)
