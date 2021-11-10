# Решение с помощью включения for

dict = {'test':'testvalue', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_dict = {key + str(len(key)): value for (key, value) in dict.items()}
dict.clear()
dict.update(new_dict)
print(dict)

# Решение с помощью прохода for

dict_v2_1 = {'test':'testvalue', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_keys_v2 = list(dict_v2_1.keys())
for i in dict_keys_v2:
    j = i + str(len(i))
    dict_v2_1[j] = dict_v2_1[i]
    dict_v2_1.pop(i)
print(dict_v2_1)

# Решение с помощью while

dict_v3_1 = {'test':'testvalue', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_keys_v3 = list(dict_v3_1.keys())
n = 0
while n < len(dict_keys_v3):
    k = dict_keys_v3[n] + str(len(dict_keys_v3[n]))
    dict_v3_1[k] = dict_v3_1[dict_keys_v3[n]]
    dict_v3_1.pop(dict_keys_v3[n])
    n += 1
print(dict_v3_1)
