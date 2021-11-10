from random import randint

# Инициализация списка с рандомными значениями
arr = [randint(1, 100) for i in range(0, 19)]

# Нахождение максимального значения в списке
max_number = max(arr)

# Копирование списка и замена его значений по условию задачи
new_arr = arr[:]
len_of_arr = len(new_arr)
n = 0
while n < len_of_arr:
    if new_arr[n] % 2 == 0:
        new_arr[n] = max_number
    n += 1
print(new_arr, len(new_arr))