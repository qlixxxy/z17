new_str = input('Введи строку')
str_len_divided = int(len(new_str) / 2)
index_key = new_str[(str_len_divided)]
print(index_key)
first_key = new_str[0]
if first_key == index_key:
    index_str = new_str[1:-1]
    print(index_str)