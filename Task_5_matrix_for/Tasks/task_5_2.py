number = input('Введите число')
sum = 0
product = 1
for x in number:
    sum += int(x)
    product *= int(x)
print(sum, product)