n = int(input('Введи начальное значение'))
m = int(input('Введи конечное значение'))
sum = 0
for i in range(n, m + 1):
    i **= 3
    sum += i
print(sum)
