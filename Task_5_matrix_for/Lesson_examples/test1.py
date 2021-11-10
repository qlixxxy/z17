# Создание квадртаное матрицы с рандомными значениями

from pprint import pprint
from random import randint
i = 6
arr = []
sum = 0
sum1 = 0
count = 0
for k in range(i):
    in_arr = []
    for k in range(i):
        k = randint(1, 9)
        in_arr.append(k)
        if k == 7:
            sum += 1
    arr.append(in_arr)
print(sum)

# Создать двумерный массив n x m


