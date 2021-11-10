# С использованием цикла for


arr = list(range(0, 15))
arr[0] = 1
n = 0
for i in arr:
    if arr.index(i, n, len(arr)) >= 2:
        j = arr[arr.index(i, n, len(arr)) - 1] + arr[arr.index(i, n, len(arr)) - 2]
        arr[arr.index(i, n, len(arr))] = j
    n += 1
print(arr)


# С использованием цикла while

arr_v2 = list(range(0,15))
arr_v2[0] = 1
n = 0
while n < len(arr_v2):
    if n >= 2:
        arr_v2[n] = arr_v2[n - 1] + arr_v2[n - 2]
    n += 1
print(arr_v2)


# СДЕЛАТЬ С ПОМОЩЬЮ a, b = b, a + b

a = 1
b = 1
k = 0
v = 15
empty_arr = [a, b]
while k < v:
    a, b = b, a + b
    k += 1
    empty_arr.append(a)
print(empty_arr)
