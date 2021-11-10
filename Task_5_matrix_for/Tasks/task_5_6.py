arr = [1, 2, 3, 4, 5, 1, 2, 7, 1, 1, 1, 1, 2, 1, 1]
counter = 0
step = 1
len_of_arr = len(arr)
while step < len_of_arr:
    if arr[step] >= arr[step - 1]:
        step += 1
    else:
        counter += 1
        step += 1
print(counter)