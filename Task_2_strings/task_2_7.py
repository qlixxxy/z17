from types import new_class


list = [1, 2, 3, 4, 3, 1]
new_set = (set(list))
new_list = [*new_set]
print(new_list)