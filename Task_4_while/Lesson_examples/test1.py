sum = 0
while True:
    x = input('Введи число')
    if x == 'stop':
        break
    elif float(x) % 5 == 0:
        continue
    else:
        sum += float(x)
print(sum)