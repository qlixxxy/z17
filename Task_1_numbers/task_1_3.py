import math
rib_length = 2
first_method_capacity = rib_length ** 3
first_method_area = 4 * (rib_length ** 2)
second_method_capacity = math.pow(rib_length,3)
second_method_area = 4 * math.pow(rib_length,2)
print(f'Capacity of a cube = {first_method_capacity}, Area of cube = {first_method_capacity}')
print(first_method_capacity == second_method_capacity, first_method_area == second_method_area)