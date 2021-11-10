# Первый способ через for


arr_v1_1 = list(range(0, 50))
arr_v1_2 = [x for x in arr_v1_1 if x % 2 == 0 and x != 0]
quantity_v1 = len(arr_v1_2)
print(quantity_v1)

# Второй способ через while


arr_v2_1 = list(range(0, 50))
counter = 0
i = 0
while i < len(arr_v2_1):
    if arr_v2_1[i] % 2 == 0 and arr_v2_1[i] != 0:
        counter += 1
    i += 1
print(counter)