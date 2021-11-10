while True:
    X = float(input('Введите X'))
    Y = float(input('Введите Y'))
    sign = input('Введите знак операции')
    if sign != '0':
        if sign == '+':
            Z = X + Y
            print(Z)
        elif sign == '-':
            Z = X - Y
            print(Z)
        elif sign == '*':
            Z = X * Y
            print(Z)
        elif sign == "/":
            if Y == 0:
                print('На ноль делить нельзя, дурачек')
            else:
                Z = X / Y
                print(Z)
        else:
            print('Введен неверный знак операции')
    else:
        print('Операция прекращена по желанию пользователя')
        break
print('Конец программы')
