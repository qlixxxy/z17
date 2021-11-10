
list = [1, 15, 20, 4, 6, 30]
new_list = [x for x in list if x > 10]
print(sum(new_list))

sum = 0
i = 0
while i < len(list):
    if list[i] > 10:
        sum += list[i]
    i += 1
print(sum)

