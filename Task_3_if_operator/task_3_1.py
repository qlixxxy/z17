new_input = input('Введи число')
new_int = int(new_input)
if new_int % 1000 == 0:
    print('millenium')
else:
    print('Остаток = {}'.format(new_int % 1000))