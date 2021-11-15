def function1(x):
    return x * 2.54 

def function2(x):
    return x / 2.54

def function3(x):
    return x * 1.609

def function4(x):
    return x / 1.609

def function5(x):
    return x / 2.205

def function6(x):
    return x * 2.205

def function7(x):
    return x * 28.35

def function8(x):
    return x / 28.35

def function9(x):
    return x * 3.785

def function10(x):
    return x / 3.785

def function11(x):
    return x * 1.759

def function12(x):
    return x / 1.759

def main():
    while True:
        y = int(input('Введите номер функции от 1-12. 0 - завершить программу'))
        if y == 0:
            return 'Программа завершена'
        x = float(input('Введите значение, которое желаете сконвертировать'))
        if y == 1:
            print(function1(x))
        elif y == 2:
            print(function2(x))
        elif y == 3:
            print(function3(x))
        elif y == 4:
            print(function4(x))
        elif y == 5:
            print(function5(x))
        elif y == 6:
            print(function6(x))
        elif y == 7:
            print(function7(x))
        elif y == 8:
            print(function8(x))
        elif y == 9:
            print(function9(x))
        elif y == 10:
            print(function10(x))
        elif y == 11:
            print(function11(x))
        elif y == 12:
            print(function12(x))
        else:
            print('Введен неккоректный номер функции')

print(main())