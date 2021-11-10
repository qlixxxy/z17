
# С использованием цикла for

arr = [4, 1, 1, 4, 4, 4, 7, 8, 9, 10]
empty_arr = []
for i in arr:
    empty_arr.insert(arr.index(i) - 1, i)
print(empty_arr)

# С использованием while

arr_v2 = [4, 1, 1, 4, 4, 4, 7, 8, 9, 10]
empty_arr_v2 = []
n = 0 
while n < len(arr_v2):
    empty_arr_v2.insert(n - 1, arr_v2[n])
    n += 1
print(empty_arr_v2)