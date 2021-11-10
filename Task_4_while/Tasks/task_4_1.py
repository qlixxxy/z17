import collections

# Первый способ через for:


arr_v1_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_v1_2 = [x * -2 for x in arr_v1_1]
print(arr_v1_2)

# Второй способ через while:

arr_v2_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_v2_2 = []
n = 0
while n < len(arr_v2_1):
    arr_v2_2.append(arr_v2_1[n] * -2)
    n += 1
print(arr_v2_2)

