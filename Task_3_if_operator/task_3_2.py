guest_quantity = int(input('Введи количество гостей'))
if guest_quantity > 50:
    print('Ресторан')
elif 20 < guest_quantity < 50:
    print('Кафе')
else:
    print('Дома')