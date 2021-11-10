from pprint import pprint
from random import randint

n = 4
m = 5
sum1 = 0
count = 0
arr = []
for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(0, 9)
        arr1.append(p)
    arr.append(arr1)
print(arr)


for k in range(n):
    for v in range(m):
        sum1 += arr[k][v]
        count += 1
print(sum1, count)

sredn_znach = sum1 / count
counter_final = 0

for k in range(n):
    for v in range(m):
        if arr[k][v] > sredn_znach and (k + v) % 2 == 0:
            counter_final += 1
print(counter_final)

