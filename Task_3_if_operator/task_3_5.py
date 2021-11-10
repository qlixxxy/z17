from math import sqrt
a = float(input('Введи а')) 
b = float(input('Введи b')) 
x = float(input('Введи x'))
c = float(input('Введи c')) 
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    first_x = (- b - sqrt(discriminant)) / 2 * a
    second_x = (- b + sqrt(discriminant)) / 2 * a
    print(f'Первый корень - {first_x},\nВторой корень - {second_x}')
elif discriminant == 0:
    first_x = (-b - sqrt(discriminant)) / 2 * a
    print(f'Один действительный корень - {first_x}')
else:
    print('Уравнение не имеет действительных корней')
