new_str = str(input('Введите предложение'))

arr = new_str.split()
arr.reverse()
final_arr = ' '.join(arr)
print(final_arr)