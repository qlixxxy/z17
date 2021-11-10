import math
x = 7
y = 17
first_method = (abs(x) - abs(y)) / (1 + abs(x * y))
second_method = (math.fabs(x) - math.fabs(y)) / (1 + math.fabs(x * y))
print(f'Result of the first method = {first_method}, Result of the second method = {second_method}, Are they equal? {first_method == second_method}')
