new_input = input('Введи строку')
str_len = len(new_input)
if str_len > 10:
    new_str = new_input + '!!!'
    print(new_str)
else:
    print(new_input[1])