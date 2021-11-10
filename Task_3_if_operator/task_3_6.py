adress = input('Введите адрес')
if adress.endswith('@gmail.com'):
    print(adress)
else:
    print(f'{adress} - неподдерживаемый формат почтового ящика')