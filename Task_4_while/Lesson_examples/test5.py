A = int(input('Введи начальное значение'))
B = int(input('Введи конечное значение'))
if A < B:
    arr = list(range(A, B + 1))
    n = len(arr)
    print(f'Список - {arr}\n, количество элементов = {n}')
else:
    print(f'{A} > {B}')
